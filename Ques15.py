#Write a program that reads data from a CSV file and prints it to the
#console

import csv
file_name = 'example.csv'

with open(file_name, mode='r') as file:
    
    csv_reader = csv.reader(file)
    
    
    for row in csv_reader:
        
        print(row)
