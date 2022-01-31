from bs4 import BeautifulSoup

import requests

# src=requests.get('https://curiosityishere.pythonanywhere.com/login/').text
src=requests.get('http://127.0.0.1:8000/login/').text
soup=BeautifulSoup(src,'lxml')
# print(soup.prettify())
body=soup.find('body')
div=body.find('div',class_='container')
token=soup.find('input',attrs={'name':'csrfmiddlewaretoken'})['value']
print(token)