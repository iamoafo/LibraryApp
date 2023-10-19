#reads in subject and classmarks from csv file
import csv

#Reads in the subject csv file 
try:
    subjectRows=[]
    with open('Subject.csv', 'r') as f:
            for row in csv.reader(f):
                subjectRows.append(row)
              
            
               
except IOError:
    print("There is a problem with the subject CSV file ")



#Reads in the location csv file
try:
    locrows=[]
    with open('Location.csv', 'r') as f:
            for row in csv.reader(f):
                locrows.append(row)
             
except IOError:
    print("There is a problem with the location CSV file ")








