import pickle
import numpy as np 


file='/Users/samir/Desktop/Desktop/programs/Python/DataSCINE/text_.txt'
file_input='/Users/samir/Desktop/Desktop/programs/Python/DataSCINE/decoded_data'

list_=[]
with open(file_input,'rb') as decode_file:
    x=decode_file.readlines()
    
    
pic_out=open("mypicklefile","wb")

#write object to file mypicklefile
pickle.dump(x,pic_out)

pic_out.close()
    