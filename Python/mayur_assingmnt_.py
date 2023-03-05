import requests
# from bs4 import BeautifulSoup
# from typing import Dict, List
# import csv

# #QUE-1
# if not os.path.exists("shakespeare_plays"):
#     os.mkdir("shakespeare_plays")

# API_URL = "http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/"
# MAX_FILES = 5

# def downloaded_files():
#     response = requests.get(API_URL)
#     soup = BeautifulSoup(response.content, "html.parser")

#     links = soup.find_all("a", href=True)
#     play_links = [link for link in links if link.get("href").endswith(".txt")]

#     for i, link in enumerate(play_links[:MAX_FILES]):
#         file_API_URL = API_URL + link.get("href")
#         response = requests.get(file_API_URL)
#         file_name = "shakespeare_plays/{}_{}".format(i+1, link.text)
#         with open(file_name, "wb") as f:
#             f.write(response.content)
#             print("Downloaded {}".format(file_name))
 
# downloaded_files()  