import os
import requests
from bs4 import BeautifulSoup
from typing import Dict, List
import csv

#QUE-1
if not os.path.exists("shakespeare_plays"):
    os.mkdir("shakespeare_plays")

API_URL = "http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/"
MAX_FILES = 5

def downloaded_files():
    response = requests.get(API_URL)
    soup = BeautifulSoup(response.content, "html.parser")

    links = soup.find_all("a", href=True)
    play_links = [link for link in links if link.get("href").endswith(".txt")]

    for i, link in enumerate(play_links[:MAX_FILES]):
        file_API_URL = API_URL + link.get("href")
        response = requests.get(file_API_URL)
        file_name = "shakespeare_plays/{}_{}".format(i+1, link.text)
        with open(file_name, "wb") as f:
            f.write(response.content)
            print("Downloaded {}".format(file_name))
 
#downloaded_files()  

#QUE-2
def create_dictionary() -> Dict:
    result = {}
    characters = []
    number_of_words_per_character = {}
    
    def remove_unessential_characters(word):
        char = ["'", "[", "(", "]", "!", ",", ":", ")", "."]
        for c in char:
            word = word.replace(c, "")
        return word
        
    
    def get_character(words: List[str]) :
        if len(words) == 0 :
            return
        word = remove_unessential_characters(words[0]);
        if word.isupper() and len(word) != 1 and word not in ("ACT", "SCENE", "SONG", "THE", "AS", "SIR", "BOTH"):
            characters.append(word)
            number_of_words_per_character[word] = number_of_words_per_character.get(word, 0) + len(words)

    for file_name in os.listdir("shakespeare_plays"):
        if file_name.endswith(".txt"):
            with open(os.path.join("shakespeare_plays", file_name), "r") as f:
                lines = {}
                for i, line in enumerate(f, 1):
                    words = line.strip().split()
                    get_character(words)
                    word_count = len(words)
                    lines[i] = word_count
                result[file_name] = lines
                
    print(number_of_words_per_character)
    return result, characters, number_of_words_per_character
           




#QU3-3
def get_lines_more_than_10_lines(response: Dict):
    
    def get_line_count(lines: Dict) -> int:
        count = 0
        for words in lines.values():
            if words >= 10: count += 1
        return count
    
    result = 0
    for value in response.values():
        result += get_line_count(lines=value)
    
    return result

#QUE-6
def create_csv_files():
    file_info = []
    for file_name in os.listdir("shakespeare_plays"):
        if file_name.endswith(".txt"):
            file_path = os.path.abspath(os.path.join("shakespeare_plays", file_name))
            file_size = os.path.getsize(file_path)
            modified_time = os.path.getmtime(file_path)
            modified_time_str = str(modified_time)
            file_info.append([file_name, file_size, modified_time_str, file_path])
    
    with open("file_info.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["File Name", "Size (bytes)", "Last Modified Datetime", "Absolute Path"])
        writer.writerows(file_info)
    
    print("CSV Files Created.!")
        

dictionary, characters, number_of_words_per_character = create_dictionary()
print(dictionary)
print(number_of_words_per_character)
