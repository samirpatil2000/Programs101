import requests
import json

# url_connect = "http://localhost:8080/web/session/authenticate"
# url = "http://localhost:8080/web/session/get_session_info"

# headers = {'Content-Type': 'application/json'}

# data_connect = {
#     "jsonrpc": "2.0", 
#     "params": {
#         "db": "odoo_db_test", 
#         "login": "9730614281", 
#         "password": "Sam"
#     }
# }

# import json
# import requests
# import sys

# AUTH_URL = 'http://localhost:8080/auth/'

# headers = {'Content-type': 'application/json'}


# # Remember to configure default db on odoo configuration file(dbfilter = ^db_name$)
# # Authentication credentials
# data = {
#     "params": {
#         "db": "odoo_db_test", 
#         "login": "9730614281", 
#         "password": "Sam"
#     }
# }

# # Authenticate user
# res = requests.post(
#     AUTH_URL, 
#     data=json.dumps(data), 
#     headers=headers
# )

# # Get response cookies
# # This hold information for authenticated user
# cookies = res.cookies
# print(str(cookies))
# # data = {}

# session = requests.Session()

# r = session.post(url=url_connect, data=json.dumps(data_connect), headers=headers)

# # print(r.json())
# if r.ok:
#     result = r.json()['result']
#     print(result)
#     print(result.get('session_id'),"Session")
#     #     session.cookies['session_id'] = result.get('session_id')

# r = session.post(url=url, data=json.dumps(data), headers=headers)
# print(r)
# print(r.json())import request

response = requests.post("https://api.localxpose.io/tunnels", json={
  "hostname": "samir-patil",
  "protocols": [
    {
      "protocol": "http",
      "port": 8000
    }
  ]
}, headers={
  "Authorization": "Bearer Y5O7bcDnbmvfXJG3cxpLYxZblj65O0gZu7sI1aDR"
})
tunnel_url = response.json()
print(tunnel_url)
