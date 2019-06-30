# Read from XML.
import xml.etree.ElementTree as ET

file_path = r"code/Day_04/data_files/data.xml"
f = ET.parse(file_path)

print("type(f): ", type(f))

# get the root.
root = f.getroot()

print("type(root): ", type(root))

print("---" * 30)
for i in root.iter():
    print(i.tag)
    print(i.text)
    print("---" * 5)
print("---" * 30)

# iterate over a column.
print("---" * 30)
for i in root.iter("Name"):
    print(i.text)
print("---" * 30)
