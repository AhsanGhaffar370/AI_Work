import bs4
import requests

url = "https://www.imdb.com/list/ls041286159/"
data=requests.get(url)
soup= bs4.BeautifulSoup(data.text, 'html.parser')

# print(soup.prettify())

for para in soup.find_all('a'):
    print(para)
    print("\n")