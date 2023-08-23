#python -m pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

url = "https://pixelford.com/blog/"
response = requests.get(url, headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'})
#print(response.content) 
#print(response) 
#print(requests.utils.default_headers())
html = response.content
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('a', class_="entry-title-link")

for a_tag in a_tags:
    print(a_tag.get_text())
