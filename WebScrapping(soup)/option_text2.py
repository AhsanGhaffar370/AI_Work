import bs4
import requests
import csv

url = "https://www.randomphonenumbers.com/Generator/us_phone_number?state=CA&city="
data=requests.get(url)
soup= bs4.BeautifulSoup(data.text, 'html.parser')

count = 0

with open('US_States.txt', mode='w') as obj: #yha close ka func use krne ki zarorat ni
    for value in soup.find_all('option'):
        name=value.text
        code=value.get('value')
        print(name,code)

        obj.write(name+", "+code+"\n")
