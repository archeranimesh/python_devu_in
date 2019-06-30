import csv

# Write into a CSV file.
file_path = r"code/Day_04/data_files/data_write.csv"

with open(file_path, "w") as f:
    cwo = csv.writer(f)
    cwo.writerow([45, 1.5])
