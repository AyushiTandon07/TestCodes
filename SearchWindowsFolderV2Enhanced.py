import os
import re
import openpyxl

def search_text_in_files(search_directory, search_text, extensions=(".sql", ".py", ".txt", ".xlsx")):
    hidden_files = []
    searchable_files = []
    unread_files = []
    results = []
    oversized_files = []
    skipped_dirs = []
    skip_dirs = ["decommissioned", "bkp", "backup", "bckp"]

    if not os.path.isdir(search_directory):
        print("Directory does not exist")
        return

    search_pattern = re.compile(re.escape(search_text), re.IGNORECASE)

    def scan_directory(path):

        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.endswith(extensions):
                    if entry.name.startswith("~$"):
                        hidden_files.append(entry.path)
                    elif os.path.getsize(entry.path) > 100 * 1024 * 1024:  # 100MB      i.e. 100000 kb  1 kb = 1024 bytes , 1 MB= 1024 kb = 1024*1024 and 100 mb = 100 * 1024 * 1024
                        oversized_files.append(entry.path)
                    else:
                        searchable_files.append(entry.path)
                elif entry.is_dir():
                    if any(skip_word in entry.name.lower() for skip_word in skip_dirs):
                        skipped_dirs.append(os.path.abspath(entry.path))  # ⬅️ Log skipped directory
                        continue
                    scan_directory(entry.path)

    def search_in_file(files):
        for file_path in files:
            try:
                if file_path.endswith((".sql", ".py", ".txt")):
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        for line_number, line in enumerate(f, 1):
                            if search_pattern.search(line):
                                results.append(f"Match found in {file_path} at line {line_number}: {line.strip()}")

                elif file_path.endswith(".xlsx"):
                    try:
                        wb = openpyxl.load_workbook(file_path, data_only=True)
                        for sheet in wb.worksheets:
                            for row in sheet.iter_rows():
                                for cell in row:
                                    if cell.value and search_pattern.search(str(cell.value)):
                                        results.append(f"Match found in {file_path} (Sheet: {sheet.title}, Cell: {cell.coordinate}): {cell.value}")
                    except Exception as e:
                        print(f"Could not open Excel file {file_path}: {e}")
                        unread_files.append(file_path)

            except Exception as e:
                print(f"Could not read {file_path}: {e}")
                unread_files.append(file_path)

    # Perform search
    scan_directory(search_directory)
    search_in_file(searchable_files)

    # Write results to file
    output_path = os.path.join(os.path.expanduser("~"), "Documents", "Python", "Search Results", "test.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")

        if unread_files:
            file.write("\n----- Unable to Open Files: Check Manually -------\n")
            for i, unread in enumerate(unread_files):
                file.write(f"{i} - {unread}\n")

        if oversized_files:
            file.write("\n----- Files Skipped (Over 100MB) -------\n")
            for i, big_file in enumerate(oversized_files):
                file.write(f"{i} - {big_file}\n")

        if skipped_dirs:
            file.write("\n----- Skipped Folders (Decommissioned/Backup/etc.) -------\n")
            for i, folder in enumerate(skipped_dirs, 1):
                file.write(f"{i} - {folder}\n")



    print("Search completed. Results saved to:", output_path)


if __name__ == "__main__":
    search_directory = input("Enter absolute directory path to search in: ").strip('"')
    search_text = input("Enter the text you want to search: ").strip()
    search_text_in_files(search_directory, search_text)
