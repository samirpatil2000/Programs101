from datetime import datetime, timedelta

# x="02/09/2021"
# print(today:=datetime.today())
# print(x:=datetime.strptime(x, "%d/%m/%Y"))
# y={"msg": "policy enddate can't be less that "+str(format(today.date()))}
# print(y)
# if x>=datetime.today():
#     print("##")
# else:
#     print("%%")

# policy_enddate="01/09/2021"
# today = datetime.today()
# # if policy_enddate
# if datetime.strptime(policy_enddate, "%d/%m/%Y")<today:
#     y={"msg": "policy enddate can't be less that "+str(today.date())}
#     print(y)


from datetime import datetime

x=datetime.today() # --> 2021-09-30 12:58:49.328148
print(x)
x=datetime.today().strftime('%d/%m/%y') # "30/09/21"
print(x)

today=datetime.today()+timedelta(days=15) #.strftime("%d-%m-%Y")
end_date=today+timedelta(days=2*365-1)

print(today.strftime("%d-%m-%y"),end_date.strftime("%d-%m-%y"))
