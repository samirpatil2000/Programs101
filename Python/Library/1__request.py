import requests
from bs4 import BeautifulSoup


# # url='https://curiosityishere.pythonanywhere.com/'
# url='http://localhost:8080/'

# LOGIN_ROUTE = 'en/web/login'

# HEADERS={  #this is stop automation
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
#     'Origin':url,
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Referer' : 'http://localhost:8080/en/web/login'
# }
# s = requests
# req = s.get('http://localhost:8080/en/web/login')
# print(req)

# print(req)

# # USERNAME='8971182182'
# # PASSWORD='Tech@Semaai123!'

# # LOGIN_DATA = {
# #     'username': USERNAME,
# #     'password': PASSWORD,
# #     'csrfmiddlewaretoken':csrf_token_,
# # }

# # login_redirect=s.post(url+LOGIN_ROUTE,headers=HEADERS,data=LOGIN_DATA)

# # print(login_redirect)
# # print(login_redirect.content)


# import requests

# url = "https://jsonmock.hackerrank.com/api/countries/search?region=Asia&name=ab&page=0"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)
# import json

# # print(response.text)
# # print(json.loads(response.text)["data"])
# print(response.status_code, type(response.status_code))