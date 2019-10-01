import bs4
import requests

url = "https://www.whatmobile.com.pk/"
data=requests.get(url)
soup= bs4.BeautifulSoup(data.text, 'html.parser')

# print(soup.prettify()) print all stuff from given link of page

# for para in soup.find('a'): ##print only one anchor(a) tags from page
#     print(para)
#     print("\n")
#
# for para in soup.find_all('a'): ##print all anchor(a) tags from page
#     print(para)
#
# for para in soup.find_all('a'): ##print all anchor(a) tags from page without <a> tag
#     print(para.text)

# for links in soup.find_all('a'):
#     link=links.get('href')       ##print all links tags from page
#
#     if link[0]=="/" and link!="#":
#         print("https://www.whatmobile.com.pk"+ link)
#
#     elif link[0:5]!="https" and link!= "#":
#         print("https://www.whatmobile.com.pk/"+ link)
#
#     elif link!= "#":
#         print(link)


################################################   how to print all links of youtube video channel
url1 = "https://www.youtube.com/user/ProgrammingKnowledge/playlists"
data=requests.get(url1)
soup= bs4.BeautifulSoup(data.text, 'html.parser')

count=0
for links in soup.find_all('a'):
    link=links.get('href')       ##print all links tags from page

    if link[0:3]=="/wa" :
        count+=1
        print(count)
        print( link)
