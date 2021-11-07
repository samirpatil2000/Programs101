# import pickle

# a=[1, 2, 3, 4, 5, 6, 7]
# a=["samir","yashika"]

# # open the file for writing
# pic_out=open("mypicklefile","wb")

# #write object to file mypicklefile
# pickle.dump(a,pic_out)

# pic_out.close()




import pickle
# open the file for reading
pic_in = open("mypicklefile", "rb")
# load the object from the file into var a
a = pickle.load(pic_in)

print(*a)