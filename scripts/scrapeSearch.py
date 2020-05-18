import json
import string

import requests
from bs4 import BeautifulSoup
from tqdm import trange

search_data = []

def get_keywords(id, name):
    name = name.replace(" ","_")
    temp = requests.get("https://wiki.metakgp.org/w/"+id+":_"+name).text
    soup = BeautifulSoup(temp, 'html.parser')
    soup = soup.find_all("p")
    soup = soup[2].text
    soup = soup.translate(str.maketrans('', '', string.punctuation))
    soup = soup.split(" ")
    return soup


with open("courses.json") as fin:
    data = json.load(fin)
    temp = list(data.items())
    for k in trange(len(temp)):
        i,j = temp[k]
        try :
            id = i
            name = j[0:j.find('-')].strip()
            name = name.title()
            professor = j[j.find('-')+1:].strip()
            professor = professor.title()
            keywords = get_keywords(i,name)
            search_data.append({
                "course_id":id,
                "course_name":name,
                "keywords": " ".join(keywords),
                "professor": professor
            })
        except Exception as e:
            pass
print(len(search_data))
with open("search_data.json","w") as fout:
    json.dump(search_data, fout ,indent=4)
