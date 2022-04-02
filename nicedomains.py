from bs4 import BeautifulSoup
import requests
import urllib.request 

req = urllib.request.urlopen("https://data.iana.org/TLD/tlds-alpha-by-domain.txt")
l = ['en', 'bp', "files", "draft", 'ja', 'bp1', 'm', 'photos1', 'bp2', 'go', 'bp3', 'gouv']
for line in req: 
    l.append(line.decode("utf-8").strip().lower())

# Website URL
URL = 'https://moz.com/top500'
  
# class list set
class_list = set()
  
# Page content from Website URL
page = requests.get( URL )
  
# parse html content
soup = BeautifulSoup( page.content , 'html.parser')
l1 = []
for i in soup.find_all("a", {"class": "ml-2"}):
    x = i.get("href")
    x = x.split("://")[1]
    if x[:4] == "www.":
        x = x[4:]
    while True:
        if len(x.split(".")) == 1:
            break
        else:        
            if x.split(".")[-1] in l:
                x = x[:-len(x.split(".")[-1]) -1]
            elif x.split(".")[0] in l:
                x = x[len(x.split(".")[0]) + 1:] 
    if x not in l1:
        l1.append(x)
print(l1)