# import requests
# import json
#
# send_url = 'http://freegeoip.net/json'
# r = requests.get(send_url)
# j = json.loads(r.text)
# lat = j['latitude']
# lon = j['longitude']
# print(" the latitude is ",lat ,"\nthe lon is ",lon)
import geocoder
g = geocoder.ip('me')
print(g.latlng)
