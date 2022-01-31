

while(True):
    try:
        userdata=input("Enter the number :\n")
        usernumber=int(userdata)
    except ValueError:
        print("please enter correct number")
    else:
        break



"""
phoebetwypb0721@gmail.com:1314520yan
casablanca0555@gmail.com:091182sarah
mukund.ganapathy@gmail.com:icici1369

lynn.cyril@gmail.com:Rosie2006
aubreypearson@yahoo.co.uk:Xx1290635
donalhahessy@yahoo.com:Grad2015
Ameliatucker77@gmail.com:Woodlawn82
robertgarrigan@hotmail.com:Uh4x6t743

"""

while(True):
    try:
        name,age,salary,address=input("Enter your name , age , address and salary").split()
        age_in_int=int(age)
        print("Your name : {0} \n age : {1} \n  address :{2} \n salary:{3}".format(name,age,address,salary))
    except:
        print("Try again \n Please Enter correct details")
    else:
        break

