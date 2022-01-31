import requests
from bs4 import BeautifulSoup
url='https://curiosityishere.pythonanywhere.com/'
#url='https://www.codechef.com'
LOGIN_ROUTE = 'login/'

headers={  #this is stop automation
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
    'origin':url, 'referer':url+LOGIN_ROUTE
}
s = requests.session()
s.get(url)
csrf_token = s.cookies['csrftoken']
print(csrf_token)



src=requests.get(url).text

soup=BeautifulSoup(src,'lxml')
token=soup.find('input',attrs={'name':'csrfmiddlewaretoken'})['value']
print(token)
login_data = {
    'csrfmiddlewaretoken':csrf_token,
    'username': 'Samir',
    'password': 'Samir@123',
}

login_req=s.post(url+LOGIN_ROUTE,headers=headers,data=login_data)
print(login_req.status_code)
cookies=login_req.cookies
print(cookies)
