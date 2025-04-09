import sys
import os, shutil
import threading
import subprocess
import fnmatch
import re
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
try:
    from PyQt5.QtWidgets import (
        QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QHBoxLayout, QMessageBox, QTextEdit
    )
    from PyQt5.QtGui import QTextCursor
except ModuleNotFoundError:
    print("Error: PyQt5 module is not installed. Please install it using 'pip install PyQt5'")
    sys.exit(1)


REPO_URL = "https://github.com/AyushiTandon07/TestCodes.git"  # Replace with actual repository
CLONE_DIR = "C:\\Users\\ayushit\\Documents\\Python\\Cloned_DIR"  # Directory to clone the repo


class GitHubSearchApp(QWidget):
    def __init__(self, repo_url, clone_dir):
        super().__init__()
        self.REPO_URL = repo_url
        self.CLONE_DIR = clone_dir
        self.init_ui()
        self.clone_repository()

    def init_ui(self):
        layout = QVBoxLayout()

        # Search Bar & Button
        search_layout = QHBoxLayout()
        # Search Directory
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Enter search query...")
        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.start_search)

        search_layout.addWidget(QLabel("Search GitHub Repo: "))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        layout.addLayout(search_layout)

        # Status Log
        self.status_log = QTextEdit()
        self.status_log.setReadOnly(True)
        layout.addWidget(self.status_log)

        # Results Table
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(2)
        self.results_table.setHorizontalHeaderLabels(["Filename", "Snippet"])
        layout.addWidget(self.results_table)

        self.setLayout(layout)
        self.setWindowTitle("Local GitHub Code Search")
        self.resize(600, 500)

    def log_status(self, message):
        self.status_log.append(message)
        self.status_log.moveCursor(QTextCursor.End)

    def is_git_installed(self):
        try:
            subprocess.run(["git", "--version"], check=True, capture_output=True, text=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def remove_readonly(self, func, path, excinfo):
        os.chmod(path, 0o777)
        func(path)

    def clone_repository(self):
        if not self.is_git_installed():
            self.log_status("Error: Git is not installed. Please install Git and try again.")
            self.show_error_message("Git is not installed. Install it from https://git-scm.com/")
            return

        self.log_status("Creating cloning directory and re-cloning repository...")
        if os.path.exists(self.CLONE_DIR):
            self.log_status("Removing existing directory...")
            shutil.rmtree(self.CLONE_DIR, onerror=self.remove_readonly)
        os.makedirs(self.CLONE_DIR, mode=0o755, exist_ok=True)

        try:
            self.log_status(f"Cloning repository into {self.CLONE_DIR}...")
            os.system('git clone ' + self.REPO_URL + ' ' + self.CLONE_DIR)
            if os.path.exists(self.CLONE_DIR) and os.listdir(self.CLONE_DIR):
                self.log_status("Repository cloned successfully.")
            else:
                self.log_status("Error: Cloning completed but no files were downloaded.")
        except subprocess.CalledProcessError as e:
            self.log_status(f"Error cloning repository: {e.stderr}")
            self.show_error_message(f"Error cloning repository: {e.stderr}")

    def search_file(self,file_path, query, pattern):
        matches = []
        try:
            # with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                # for line in f:
                #     if pattern.search(line):  # Check if line matches the regex pattern
                #         matches.append((file_path, line.strip()))
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line_num, line in enumerate(f, start=1):  # Include line number in case we need to debug
                    line = line.strip()  # Remove leading/trailing whitespace
                    if pattern.search(line):  # Check if line matches the regex pattern
                        # Print for debugging to see what's being matched
                        print(f"Match found in {file_path} on line {line_num}: {line}")
                        matches.append((file_path, line.strip(), line_num))
        except Exception as e:
            print(f"Error reading file {file_path}: {str(e)}")

    def start_search(self):
        self.log_status("Starting search...")
        threading.Thread(target=self.search_local_repo, daemon=True).start()

    def search_local_repo(self):
        query = self.search_input.text().strip()
        if not query:
            self.log_status("Search query is empty.")
            return

        # Compile the pattern with case-insensitive matching
        # pattern = re.compile(f".*{query}.*", re.IGNORECASE)
        pattern = re.compile(re.escape(query), re.IGNORECASE)

        matches = []
        self.log_status("Searching in repository files...")

        # Use ThreadPoolExecutor to search files concurrently
        with ThreadPoolExecutor() as executor:
            futures = []

            # Walk through the repo directory
            for root, _, files in os.walk(self.CLONE_DIR):
                for file in fnmatch.filter(files, "*.py"):  # Searching only Python files, modify if needed
                    file_path = os.path.join(root, file)
                    self.log_status(f"Checking file: {file_path}")
                    # Submit the search task to the executor
                    future = executor.submit(self.search_file, file_path, query, pattern)
                    futures.append(future)

            # Wait for all futures to complete and collect results
            for future in futures:
                result = future.result()  # Get the result from the future
                if result:  # Check if the result is not None
                    matches.extend(result)  # Add matches to the list

        self.log_status("Search completed.")
        self.display_results(matches)

    def display_results(self, results):
        self.results_table.setRowCount(len(results))
        for row, (filename, snippet) in enumerate(results):
            self.results_table.setItem(row, 0, QTableWidgetItem(filename))
            self.results_table.setItem(row, 1, QTableWidgetItem(snippet))

        if not results:
            self.log_status("No matches found.")

    def show_error_message(self, message):
        QMessageBox.critical(self, "Error", message)

if __name__ == "__main__":
    # REPO_URL = "https://github.com/your_username/your_repo.git"  # Replace with actual repository
    # CLONE_DIR = "C:/Users/your_username/Documents/my_repo"  # Set to absolute path

    app = QApplication(sys.argv)
    window = GitHubSearchApp(REPO_URL, CLONE_DIR)
    window.show()
    sys.exit(app.exec_())
