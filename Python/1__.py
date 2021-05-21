
# from tkinter import *   
  
# tk_ = Tk()  
  
# tk_.geometry("400x400")  
  
# #creating a simple canvas  
# canvas_ = Canvas(tk_,bg = "red",height = "200")  
  
# arc = canvas_.create_arc((5,10,150,200),start = 0,extent = 150, fill= "white")  
# canvas_.pack()  
  
# # tk_.mainloop() 



# distance=int(input("Enter the distance in km : "))

# meter = distance * 1000
# Feet = distance * 3280.84
# Inches = distance * 39370.1
# Centimeter = distance * 100000


# print("Distance in meter ",meter)
# print("Distance in Feet ",Feet)
# print("Distance in Inches ",Inches)
# print("Distance in Centimeter ",Centimeter)



string= input ("Enter the string: ")
newlist = list(string)
print(newlist)
dict_={'Lower':0,'Upper':0}
for i in newlist:
    if i!=" ":
        if i.islower():
            dict_['Lower']+=1
        else:
            dict_['Upper']+=1
    
print("Number of lower letters are: ",dict_['Lower'])
print("Number of upper letters are: ",dict_['Upper'])