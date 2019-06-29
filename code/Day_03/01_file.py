import os

file_name = r"/pythonFile01.txt"

# https://stackoverflow.com/questions/1296501/find-path-to-currently-running-file
def get_file_path():
    dirname, _ = os.path.split(os.path.abspath(__file__))
    return dirname


print(get_file_path())

full_file_path = get_file_path() + file_name

print(full_file_path)

f = open(full_file_path, "w")
print("type(f): ", type(f))
print("f.mode: ", f.mode)
print("f.name: ", f.name)
print("f.readable(): ", f.readable())
print("f.writable(): ", f.writable())
print("f.closed: ", f.closed)

f.close()
