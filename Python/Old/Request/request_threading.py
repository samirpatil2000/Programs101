import requests
import time


url='https://dl1.drbox.xyz/Series/The%20Flash/S06/The.Flash.S06E18.480p.HDTV.x264.TagName.mkv'
#url='https://curiosityishere.pythonanywhere.com/login/'

headers={  #this is stop automation
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
    'origin':url, 'referer':url
}

r = requests.get(url,headers=headers)

# print(dir(r))
# print(help(r))

print(r.status_code)

t1=time.perf_counter()

# for