import os,sys
folder = '/Users/samir/Desktop/LIFE'
for filename in os.listdir(folder):
    print(filename)
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('', '.jpeg')
    output = os.rename(infilename, newname)