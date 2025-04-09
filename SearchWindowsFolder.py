import os, re
import openpyxl
import zipfile
from zipfile import BadZipfile

hiddenFilesList = []
searchableFilesList = []
UnreadFilesList = []

def search_text_in_files(search_directory, search_text, extensions=(".sql", ".py", ".txt", ".xlsx")):
    """Search for a string in .sql, .py, .txt, and .xlsx files using os.scandir()."""

    CheckDir= os.path.isdir(search_directory)
    if not CheckDir:
        print("Directory does not exist")


    search_pattern = re.compile(re.escape(search_text), re.IGNORECASE)

    def scan_directory(path):
        global hiddenFilesList, searchableFilesList

        with os.scandir(path) as entries:           #os.scandir() function returns entries in a given directory/path
            for entry in entries:
                if entry.is_file() and entry.name.endswith(extensions):     # os.name() function Retrieves the filename from the os.scandir() entry.
                    if entry.name.startswith("~$"):
                        hiddenFilesList.append(entry.path)

                    else:
                        searchableFilesList.append(entry.path)
                    # search_in_file(entry.path, search_text)
                elif entry.is_dir():
                    scan_directory(entry.path)


            # print("----- Hidden Files List: -----", hiddenFilesList)
            # print("\n\n------ Searchable Files List: ------", searchableFilesList)


    def search_in_file(searchableFilesList, search_text):
        global UnreadFilesList


        with open('C:\\Users\\ayushit\\Documents\\Python\\Search Results\\test.txt', 'w') as file:
            for i in range(0, len(searchableFilesList)):
                file_path = searchableFilesList[i]
                """Search for text inside a file, handling both text and Excel files."""
                try:
                    if file_path.endswith((".sql", ".py", ".txt")):  # Text-based files
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                            for line_number, line in enumerate(f, 1):
                                if search_pattern.search(line):
                                    # print("Match found in {} at line {}: {}".format(file_path, line_number, line.strip()))
                                    file.write("Match found in {} at line {}: {}\n".format(file_path, line_number, line.strip()))


                    elif file_path.endswith(".xlsx"):  # Excel files
                        try:
                            wb = openpyxl.load_workbook(file_path, data_only=True)
                        except Exception as e:
                            print(f"Failed to open {file_path} — {type(e).__name__}: {e}")


                        for sheet in wb.worksheets:
                            for row in sheet.iter_rows():
                                for cell in row:
                                    if cell.value and search_pattern.search(str(cell.value)):
                                        # print("Match found in {} (Sheet: {}, Cell: {}{}): {}".format(
                                        #     file_path, sheet.title, cell.column_letter, cell.row, cell.value))
                                        file.write("Match found in {} (Sheet: {}, Cell: {}{}): {} \n".format(
                                            file_path, sheet.title, cell.column_letter, cell.row, cell.value))


                except Exception as e:
                    print("Could not read {}: {}".format(file_path, e))
                    UnreadFilesList.append(file_path)



    scan_directory(search_directory)
    search_in_file(searchableFilesList, search_text)
    with open('C:\\Users\\ayushit\\Documents\\Python\\Search Results\\test.txt', 'a') as file:

        if len(UnreadFilesList) >0:
            file.write("----- Unable to Open Files: Check Manually ------- \n")
            for i in range(0,len(UnreadFilesList)):
                file.write(f"{i}- {UnreadFilesList[i]}\n")



    # print("----- Hidden Files List: -----", hiddenFilesList)
    # print("\n\n------ Searchable Files List: ------", searchableFilesList)



if __name__ == "__main__":
    # search_directory = r"W:\DFS\DFS PDS\GNA"  # Change as needed
    # search_text = "seleCT"  # Change your search text
    search_directory = input("Enter absolute directory path to search in: ")
    search_text = input("Enter the text you want to search: ")
    search_text_in_files(search_directory, search_text)



