import requests
import json
# url = "https://jsonmock.hackerrank.com/api/countries/search?region=Asia&name=ab&page=0"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)


# # print(response.text)
# # print(json.loads(response.text)["data"])
# print(response.status_code, type(response.status_code))

def call_api(page):
    url = "https://jsonmock.hackerrank.com/api/medical_records?page={}".format(page)
        
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)

def find_rate(response, diagnosisName, doctorId):   
    result = 0
    ave = 0
    for i in range(len(response["data"])):
        curr_data = response["data"][i]
        if curr_data["diagnosis"]["name"] == diagnosisName and curr_data["doctor"]["id"] == doctorId:
            result += curr_data["vitals"]["pulse"]
            ave += 1

    return result, ave
    
def pulse_rate(diagnosisName, doctorId):
    response = call_api(1)
    total_pages = response["total_pages"]
    result, ave = find_rate(response, diagnosisName, doctorId)
    
    for page in range(2, total_pages + 1):
        new_response = call_api(page)
        if new_response.get("data"):
            res_ave =  find_rate(new_response, diagnosisName, doctorId)
            result += res_ave[0]
            ave += res_ave[1]
    return result // ave


print(pulse_rate("Pulmonary embolism", 2))