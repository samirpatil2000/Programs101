filename='file'
filename1='sam'

with open(filename) as f_obj:
    lines=f_obj.readlines()

for line in lines:
    print(line.strip())

with open(filename1,'w') as f:
    f.write("Hey their I love hacking")

with open(filename1) as f:
    content = f.read()
print(content)



# Write csv file

while(True):
    try:
        name,age,salary,address=input("Enter your name , age , address and salary").split()
        age_in_int=int(age)
        print("Your name : {0} \n age : {1} \n  address :{2} \n salary:{3}".format(name,age,address,salary))
    except:
        print("Try again \n Please Enter correct details")
    else:
        break

with open('sam1.csv', 'w')as f:
    f.write( name+','+ address+','+salary +',' + age  )


# CSV Reader

# with open()





