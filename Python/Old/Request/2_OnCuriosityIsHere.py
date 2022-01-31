import requests

#url='https://curiosityishere.pythonanywhere.com/admin/'
url='https://tamrapat.pythonanywhere.com'
# username_and_pass={'username':'Samir','password':'Samir@123'}
# login_request=requests.post(url)
# print(login_request.status_code)
r=requests.get(url)
print(r.status_code)
#print(r.text)
print(r.cookies)
# print(dir(r))
# print(help(r))

print("r.links ==>",r.links)


#list=[]
# for _ in range(2):
#     r = requests.get(url)
#     cokies=r.cookies
#     list.append(cokies)
#     print(cokies)
# print(list)
# print(list[0][1])




