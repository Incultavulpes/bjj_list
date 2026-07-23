import requests as re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
}

URL_TEMPLATE = "https://bjjfanatics.com/collections/instructional-videos/fighter_{fighter_name}?list={list_number}"

for list_number in range(1, 6):    
    response = re.get(URL_TEMPLATE.format(fighter_name= "gordon-ryan", list_number= list_number), headers=headers)
    print(response.status_code)