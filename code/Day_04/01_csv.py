import pandas as pd

# Read CSV using pandas.
file_path = r"code/Day_04/data_files/data.csv"

df = pd.read_csv(file_path)
print("DF: \n", df)
print("DF['EMAIL']:\n", df["Email"])
print("df.ndim: ", df.ndim)  # dimesions of data
