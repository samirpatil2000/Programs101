# your_list='SsamirPatil@1234567890'
# complete_list=[]
number='1234567890'
symbols='@#$&*'


# name=input("Name :")
# surname=input("Surname :")
# nickname=input("Nickname :")
name="samir"
surname="patil"


password_list=[]


def filterRPL(password,list):
    if password in list:
        pass
    else:
        print(password)
        list.append(password)
    return list

for x in range(len(name)):
    # for i in range(len(symbols)):
    #     password7=name[:x+2]+
    for j in range(99,999):

        for symbol in symbols:
            password7=name[:x+2]+surname+symbol+str(j)
            password8=symbol+name[:x+2]+surname+str(j)
            password9=symbol+name[:x+2]+str(j)
            password10 = name[0].upper()+name[1:]+surname+symbol+str(j)
            password11 = name[0].upper()+name[1:x+2]+surname+symbol+str(j)
            password12 = name[0].upper()+name[1:x+2]+surname[0].upper()+surname[1:]+symbol+str(j)
            password13 = symbol+name[0].upper()+name[1:x+2]+surname+symbol+str(j)
            password15=name[:x+1].upper()+surname+symbol+str(j)

            filterRPL(password7,password_list)
            filterRPL(password8,password_list)
            filterRPL(password9,password_list)
            filterRPL(password10,password_list)
            filterRPL(password11,password_list)
            filterRPL(password12,password_list)
            filterRPL(password13,password_list)
            filterRPL(password15,password_list)



            # password_list.append(password7)
            # password_list.append(password8)
            # password_list.append(password9)
            # password_list.append(password10)
            # password_list.append(password11)
            # password_list.append(password12)
            # password_list.append(password13)
            # password_list.append(password15)

        password1=name[:x+2]+surname[:]+str(j)
        password5=name[0].upper()+name[1:]+surname.lower()+str(j)
        password2=name[0]+surname+str(j)
        password3=surname+str(j)
        password4=surname+name[:x+2]+str(j)
        password14=surname[0].upper()+surname[1:]+name[:x+2]+str(j)
        # password6=nickname=
        # password_list.append(password1)
        # password_list.append(password2)
        # password_list.append(password3)
        # password_list.append(password4)
        # password_list.append(password5)
        # password_list.append(password14)
        filterRPL(password1,password_list)
        filterRPL(password2,password_list)
        filterRPL(password3,password_list)
        filterRPL(password4,password_list)
        filterRPL(password5,password_list)
        filterRPL(password14,password_list)
        # print(password1)
        # print(password2)
        # print(password3)
        # print(password4)
        # print(password5)

#print(password_list)
y='Sampatil@123'
def checkingPassword():
    if y in password_list:
        print('Yes it is ',y)
    else:
        print(y ,"y is not in the list")

checkingPassword()

def filteringReapetedPassword(password_list):
    main_list=[]
    count=0
    for y in password_list:
        if y not in  main_list:
            main_list.append(y)
            count=count+1
            print(count)

    return main_list
#print("This is the filetr list")
print(password_list)
print("The length of the list is ",len(password_list))
#filteringReapetedPasswordList=filteringReapetedPassword(password_list)
#print(filteringReapetedPasswordList)
#print("the length of filtered list {} and the non filtered list {}".format(len(filteringReapetedPasswordList),len(password_list)))









# print(name[0].upper()+name[1:]+surname+"@"+str(123))


