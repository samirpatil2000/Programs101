import requests
url='https://api.github.com/events'
#url='https://dl3.drbox.xyz/Series/The%20Boys%202019/S02/The.Boys.S02E05.480p.WEB.x264.TagName.mkv'
s = requests.session()

r=s.get(url)
print(r.text,r.content)
# json=r.json()
# print(json[0]['actor'])
# print(json[0]['actor']['login'])

print(r.status_code)

