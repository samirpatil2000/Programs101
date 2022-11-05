import requests

url = "http://localhost:8080/v1/products?search=FMC&global_products=True&offset=0&limit=4"
payload = ""
headers = {
  'Content-Type': 'text/plain; charset=UTF-8',
  'Authorization': 'Basic bWtSNjl2bmhnbXlWcEdCODpta1I2OXZuaGdteVZwR0I4',
  'Cookie': 'session_id=c07e9c4dc44c3c9682fb12924c9f2b49433f5925; session_id=71e04592fde4b64392fa0bbdb5b99c42033e9287; visitor_uuid=03c1a90388114f90a99094760b2f5801',
  'Auth': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6IjA4NzQ0ODg5ODk2In0.otneyKgNgl06axv_SanXvDSX7vfo_MB6rn8oFdQt-dg'
}

import timeit
import time

start = timeit.default_timer()

time.sleep(1)
response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)


stop = timeit.default_timer()

print('Time: ', stop - start)  

import json
print(len(json.loads(response.text)["data"]["products"]))
# Time:  9.979153123
# Time:  9.637878409 # New 

# Time:  8.688339723 Round
# Time:  9.212578791 Round Up Accurate results 

# Time:  8.999908621 Round


# (FMC):- limit 10
# Time:  14.873841224000001 New -  
# Time:  15.753511932999999

# FMC :- limit 25
# Time:  37.180232477000004 New - 
# Time:  45.628087611
start = timeit.default_timer()
stop = timeit.default_timer()

print('Time: ', stop - start)