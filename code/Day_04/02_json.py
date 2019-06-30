import json

file_path = r"code/Day_04/data_files/data_write.json"

d = {"+91": "India", "+92": "Pak", 2: True, 3: [34, 56.7, "apple", "ant", None]}

with open(file_path, "w") as f:
    json.dump(d, f, indent=4)

print("Written to JSON")
