import random
password=str(input("Enter the password : "))

geuss= " "

while geuss != password:
	geuss=str(random.randint(0,9999))
	print("==>" + geuss)
	if(geuss==password):
		print("You crack it " + password)
		break
	    

