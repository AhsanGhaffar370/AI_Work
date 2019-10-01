import bs4
import requests
url = "https://www.randomphonenumbers.com/Generator/us_phone_number?state=CA&city="
data=requests.get(url)
soup= bs4.BeautifulSoup(data.text, 'html.parser')
count = 0
for value in soup.find_all('option'):
    value=value.get('value')       ##print all option tags values from page
    print( value)
