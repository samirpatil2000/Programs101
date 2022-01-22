import requests

url = "https://preprod-toko.semaai.com/mobikul/homepage/"

payload = "{ \"params\": {\n    \"data\":{}\n}}"
headers = {
  'Login': 'ewogICJsb2dpbiI6ICI4OTcxMTgyMTgyIiwKICAicHdkIjogIlRlY2hAU2VtYWFpMTIzISIKfQ==',
  'Content-Type': 'text/plain; charset=UTF-8',
  'Authorization': 'Basic bWtSNjl2bmhnbXlWcEdCODpta1I2OXZuaGdteVZwR0I4',
  'Cookie': 'session_id=6b1b4d7309c70bb59ab98ba6722b048eddcedc5b; session_id=649f62d9a3dd265e2e3c09ec5a98a529dac08f59'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
