# import requests
# #import os
# from datetime import datetime

# api_key = '12f3fe0150a34c3e74ba3e458f6e0b7d'
# location = input("Enter the city name: ")

# complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
# api_link = requests.get(complete_api_link)
# api_data = api_link.json()

# #create variables to store and display data
# temp_city = ((api_data['main']['temp']) - 273.15)
# weather_desc = api_data['weather'][0]['description']
# hmdt = api_data['main']['humidity']
# wind_spd = api_data['wind']['speed']
# date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
# file = open("example.txt", "w")
# l="-------------------------------------------------------------"
# print(l)
# file.write(str(l))
# s="Weather Stats for - {}  || {}".format(location.upper(), date_time)
# print(s)
# file.write(str((s)))
# print (l)
# l="Current temperature is: {:.2f} deg C".format(temp_city)
# file.write(str(l))
# print (l)
# l="Current weather desc  :",weather_desc
# file.write(str(l))
# print (l)
# l="Current Humidity      :",hmdt, '%'
# file.write(str(l))
# print (l)
# l="Current wind speed    :",wind_spd ,'kmph'
# file.write(str(l))
# print (l)
# file.close()
