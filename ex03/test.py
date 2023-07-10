#!/usr/bin/env python3
from csvreader import CsvReader
if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
        print(header)
        print(data)
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
            print(header)
            print(data)
