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

# Print only the Data Row.
print("---" * 30)
for item in cro[1:]:
    print(item)
print("---" * 30)

# Print a column from CSV
print("---" * 30)
for item in cro[1:]:
    print(item[2])
print("---" * 30)

# Using list comphresion.
receivers = [i[2] for i in cro[1:]]
print("---" * 30)
print(receivers)
print("---" * 30)
