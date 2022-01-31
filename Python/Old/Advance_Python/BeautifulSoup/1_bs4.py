from bs4 import BeautifulSoup
import requests


with open('sample.html') as html_file:
    soup=BeautifulSoup(html_file,'lxml')

# print(soup.prettify())
#
# print(f' The title is  -->  {soup.title.text}')
# print(f' The First Article With div class  -->  {soup.div}')
# print(f'This is the text of  The First Article is +++  {soup.div.text}')



"""Search Elements with ID , class name """

find=soup.find('div',class_='footer')
# print(find)

# article=soup.find('div',class_='article')
articles=soup.find_all('div',class_='article')
""" -- find --  will return only first result but -- find_all -- will return te list of matching results """

for article in articles:
    article_headline=article.h2.a.text
    article_headline_url=article.h2.a.href
    article_summary=article.p.text
    print(f'{article_headline} and the href is {article_headline_url} \n The Summary {article_summary}')