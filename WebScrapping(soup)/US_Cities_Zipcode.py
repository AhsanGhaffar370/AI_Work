import bs4
import requests

# url1 = "https://www.zip-codes.com/city/oh-dayton.asp"   ##Dayton city link
# url1 = "https://www.zip-codes.com/city/oh-columbus.asp"  ##Columbus city link
# url1 = "https://www.zip-codes.com/city/oh-cleveland.asp"  ##cleveland city link
url1 = "https://www.zip-codes.com/city/oh-cincinnati.asp"  ##cincinnati city link

data=requests.get(url1)
soup= bs4.BeautifulSoup(data.text, 'html.parser')

count=0

#with open('Dayton_zipcodes.txt', mode='w') as obj:   ##Dayton file
#with open('Columbus_zipcodes.txt', mode='w') as obj:   ##Columbus file
# with open('Cleveland_zipcodes.txt', mode='w') as obj:   ##Cleveland file
with open('Cincinnati_zipcodes.txt', mode='w') as obj :  ##cincinnati file
    for links in soup.find_all('a'):
        link=str(links.get('title'))       ##print all links tags from page000

00 bll        #if link[0:10] == "ZIP Code 4":   ##Dayton Zip Code Condition
        # if link[0:10] == "ZIP Code 4":   ##Columbus Zip Code Condition
        # if link[0:10] == "ZIP Code 4":  ##Cleveland Zip Code Condition
        if link[0 :10] == "ZIP Code 4" :  ##Cincinnati Zip Code Condition
            print(link)
            obj.write(link[9:14] +"\n")
