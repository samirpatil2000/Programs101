import requests
import json


def call_api(page):
    url = "https://jsonmock.hackerrank.com/api/articles?page={}".format(page)
        
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)


def add_data(data):
    result = [] # [title , comment]
    for i in range(len(data)):
        if data[i].get("title") == None and data[i].get("story_title") == None:
            continue
        title = None
        comments = data[i].get("num_comments", 0)
        if data[i].get("title"):
            title = data[i].get("title")
        else:
            title = data[i].get("story_title")
        if title != None and comments != None:
            result.append([comments, title])
    return result
    
def pulse_rate(limit):
    response = call_api(1)
    total_pages = response["total_pages"]
    
    if response.get("data"):
        
        result = add_data(response.get("data"))
    else:
        result = []
    for page in range(2, total_pages + 1):
        new_response = call_api(page)
        if new_response.get("data"):
            result.extend(add_data(new_response.get("data")))
    # print(result)
    return sorted(result, key=lambda x: [-x[0], x[1]])[:limit]            


# print(pulse_rate(2))

# list_ = [[967, 'A Message to Our Customers'], [265, 'Was isolated from 1999 to 2006 with a 486. Built my own late 80s OS'] ]
# print(sorted(list_, key=lambda x: [-x[0], x[1]])  )

from itertools import permutations
def allPermutations(str):
      
     # Get all permutations of string 'ABC'
     permList = permutations(str)
 
     # print all permutations
     for perm in list(permList):
        print (int(''.join(perm)))
         
         
print(allPermutations("234"))