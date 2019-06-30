import json

file_path = r"code/Day_04/data_files/data.json"

with open(file_path) as f:
    data = json.load(f)

print(type(data))
print(data)
