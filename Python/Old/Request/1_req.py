import requests
payload={'firstName':'Samir','lastName':'Patil'}

# THIS IS FOR GET request
#r = requests.get('https://httpbin.org/get',params=payload)
# FOR POST request
#r=requests.post('https://httpbin.org/post',data=payload)
#url='https://api.github.com/events'
url='https://dl1.drbox.xyz/Series/The%20Flash/S06/The.Flash.S06E18.480p.HDTV.x264.TagName.mkv'
r = requests.post(url)
# json=r.json()

# print(dir(r))
# print(help(r))

print(r.status_code)
# print(r.text)
# print(r.encoding)
# print(r.content)

# image_url=json[0]['actor']['avatar_url']
# img_request=requests.get(image_url)
# print(img_request.content)  # it will print in BIT
#
# # NOW YUO HAVE TO USE
#
# with open('save.png','wb') as f:
#     f.write(img_request.content)


"""https://www.udemy.com/course/ios-13-app-development-bootcamp/?gclid=EAIaIQobChMI24PswO_66wIVM9tzAR08bg1QEAEYASAAEgKH-vD_
BwE&moon=TETHYS1062&utm_campaign=INTL-YT-PROS-TECH-Dev-TOP-Q3C-IosDevelopment-EN-IND_
   ._ci_1778502_._sl_IND_._vi_TECH_._sd_All_._la_EN_._&utm_content=Overlay&utm_medium=udemyads&utm_source=youtube-intl&utm_term=_
   ._ag_106648311506_._ad_458172992876_._de_c_._dm__._pl_youtube.com_._ti__._li_9062101_._pd__._"""

# r2=requests.get()