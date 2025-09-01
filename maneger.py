import csv

def get_csv_file(file_fath):
    with open(file_fath, mode ='r')as file:
        csvFile = csv.reader(file)
        return csvFile
    