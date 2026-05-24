#read a file and handle errors
import os
try:
    with open("sample.txt","rt") as fh:
        print("Reading file content:")
        lines = fh.readlines()
        for line in lines:
            print(f"line{lines.index(line)+1}: {line.rstrip()}")

except FileNotFoundError:
    print("Error:The file 'sample.txt' was not found.")
