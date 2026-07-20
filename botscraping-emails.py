import requests
from bs4 import BeautifulSoup
import re

#Enter the url of the website 
url = "https://enteryoururl-plz.com" 

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

texte = soup.get_text()

emails = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    texte
)

for email in set(emails):
    print(email)
