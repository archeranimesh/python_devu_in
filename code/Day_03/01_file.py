import os

file_name = r"pythonFile01.txt"

# https://stackoverflow.com/questions/1296501/find-path-to-currently-running-file
def get_file_path():
    dirname, _ = os.path.split(os.path.abspath(__file__))
    return dirname


print(get_file_path())
