import csv 
from database.manager import CategoryManager

def fill_category_data(filename):
    with open(filename,"r",encoding="utf-8") as csv_file:
        rows = csv.reader(csv_file,delimiter=",")
        for r in rows:
            print(r)
            
fill_category_data('data_files/category_data.csv')
