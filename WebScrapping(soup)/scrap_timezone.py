import bs4
import requests
import csv

url = "https://www.php.net/manual/en/timezones.america.php"
data=requests.get(url)
soup= bs4.BeautifulSoup(data.text, 'html.parser')

count = 0

with open('US_timezones.txt', mode='w') as obj: #yha close ka func use krne ki zarorat ni
    for value in soup.find_all('td'):
        name=value.text
        # code=value.get('value')

        obj.write("<option value=\""+name+"\" formula_val=\"\">"+name[8:]+"</option>\n")
        # print(obj.write("<option value=\""+name+"\" formula_val=\"\">"+name[8:]+"</option>\n"))


# <option value="America/Adak" formula_val="">Adak</option>

