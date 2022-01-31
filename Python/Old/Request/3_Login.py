import requests
from bs4 import BeautifulSoup


# url='https://curiosityishere.pythonanywhere.com/'
url='http://127.0.0.1:8000/'

LOGIN_ROUTE = 'login/'

HEADERS={  #this is stop automation
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
    'origin':url, 'referer':url+LOGIN_ROUTE
}
s = requests.session()
csrf_token = s.get(url).cookies['csrftoken']
# print(csrf_token)

USERNAME='Samir'
PASSWORD='Samir@123'

LOGIN_DATA = {
    'username': USERNAME,
    'password': PASSWORD,
    'csrfmiddlewaretoken':csrf_token,
}

login_redirect=s.post(url+LOGIN_ROUTE,headers=HEADERS,data=LOGIN_DATA)

# print(login_redirect)
# print(login_redirect.status_code)
# cookies=login_redirect.cookies
# print(cookies)
# print(login_redirect.content)

redirect_url=s.get(url+'U/profile/').text

soup=BeautifulSoup(redirect_url,'lxml')
class_name=soup.find('div',class_='container')
name=soup.find('h2',attrs={'style':"margin-top:30px;"}).text

if name is not None:
    print(" Password Cracked ..! ",USERNAME," and ",PASSWORD)
else:
    print(" Something Went Wrong ")
