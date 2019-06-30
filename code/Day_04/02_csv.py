import csv

file_path = r"code/Day_04/data_files/data.csv"

with open(file_path) as f:
    cro = list(csv.reader(f))

print("CRO:\n", cro)

# Use for loop to print the rows.
print("---" * 30)
for item in cro:
    print(item)
print("---" * 30)
