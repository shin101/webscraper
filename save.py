import csv

def save_to_file():
    file = open("jobs.csv",mode="w")
    writer = csv.writer(file)
    writer.writerow("test test")
    return