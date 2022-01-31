from bs4 import BeautifulSoup
import requests
import csv

src=requests.get('http://coreyms.com').text

soup=BeautifulSoup(src,'lxml')
articles=soup.find_all('article')
i=0

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'time', 'content','video_link'])

for article in articles:
    title=article.header.h2.a.text
    time=article.header.p.time.text

    content_class=article.find('div',class_='entry-content')
    content=content_class.p.text

    try:
        """
        ALL THESE WORK SAME
        video_link=content_class.find('iframe',class_='youtube-player')['src']
        video_link=article.find('iframe',class_='youtube-player')['src']
        """
        video_link=content_class.span.iframe['src']
        """ Now you have to take only id of that yt video """
        video_id=video_link.split('/')[4]  #because split function will return list and our id is at 4th position and the link is separated by " / "
        id=video_id.split('?')[0]
        yt_link=f'https://youtube.com/watch?v={id}'

    except Exception as e:
        yt_link=None

    i+=1

    print(i,']  ',title,"  -  "," {",time,"} ","\n",content,"\n",yt_link)

    csv_writer.writerow([title, time,content, yt_link])

csv_file.close()
