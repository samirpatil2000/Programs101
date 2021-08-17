import os,sys
# folder = '/Users/samir/Desktop/LIFE'
# for filename in os.listdir(folder):
#     print(filename)
#     infilename = os.path.join(folder,filename)
#     if not os.path.isfile(infilename): continue
#     oldbase = os.path.splitext(filename)
#     newname = infilename.replace('', '.jpeg')
#     output = os.rename(infilename, newname)

filename='/Users/samir/Desktop/Dev/Zopper/TATAAIG/Master/Previous Insurer Master.csv'
# import csv
# rows=[]
# with open(filename, 'r') as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)
      
#     # extracting field names through first row
    
#     print(csvreader)
    
#     # get total number of rows
import csv
file_='/Users/samir/Desktop/Desktop/programs/Python/people.csv'

dict_={
    
}
with open(file_, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        dict_[row[1]]={
            'code':row[0],
            'name':row[1],
        }
    print(dict_)

