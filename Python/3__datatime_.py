from datetime import datetime

x="02/09/2021"
print(today:=datetime.today())
print(x:=datetime.strptime(x, "%d/%m/%Y"))
y={"msg": "policy enddate can't be less that "+str(format(today.date()))}
print(y)
if x>=datetime.today():
    print("##")
else:
    print("%%")

policy_enddate="01/09/2021"
today = datetime.today()
# if policy_enddate
if datetime.strptime(policy_enddate, "%d/%m/%Y")<today:
    y={"msg": "policy enddate can't be less that "+str(today.date())}
    print(y)