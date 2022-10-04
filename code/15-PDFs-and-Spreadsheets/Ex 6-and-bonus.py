"""
Created on Oct 4 2022
"""
from audioop import avg
import csv
from encodings import utf_8

import os



os.chdir("D:/cognixia/learning-python/code/15-PDFs-and-Spreadsheets")
# Example
f=open("example.csv",encoding='utf_8')
lines=f.readlines() # Store as list type
for l in lines:
    print(l)

data = open("example.csv",encoding='utf-8') # TextIOWrapper type
csv_data = csv.reader(data)




# 6.1 cookbook
# Reader
# CSV read/write
with open("example.csv",encoding='utf-8') as f:
    csv_data = csv.reader(f, delimiter=',') # delimiter can be set to other characters (\t for TSV)
    header=next(csv_data)
    # header = [ re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv) ] # Substitute invalid characters in header to underscore
    print(header)
    for row in csv_data:
        print(row)
        # print(row[1]) # Get all data in 2nd column
# For loop
with open("example.csv",encoding='utf-8') as f:
    for line in f:
        row = line.split(",")
        print(row) # Get all data in all column
        # print(row[1]) # Get all data in 2nd column
# Does not understand \n as EOL in Windows
#     
# Writer:
# With CSV read/write
with open("practice_writeto.csv",'w',newline='',encoding='utf-8') as f:
    csv_data = csv.writer(f)
    csv_data.writerows([['this','is','a','header'],['this','is','first','row']])
# With loop
with open("practice_writeto_otherway.csv",'w',newline='',encoding='utf-8') as f:
    noOfRow=4
    for i in range(noOfRow):
        f.write("A,row,{}\n".format(i+1))
        
    
# # For loop vs CSV reader
# # For loop work similary with CSV header with appropriate seperator
# # For loop may run into issue when a field in csv has a seperator symbol inside the field
# # Example: CSV reader can read this but not loop: field1, "field2, still field2", field3
# # Using for loop by itself won't parse \n as end of line on Windows

