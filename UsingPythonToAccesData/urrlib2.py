#python app to scan through the web looking for certain patterns

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

web = input("Please type the web page name: ")
count = int(input("Please enter count: "))+1
upTo = int(input("Please type the index of the link you want us to follow: "))
upTo -= 1

while count > 0:
    count -= 1
    print("Actual web page:",web)
    html = urllib.request.urlopen(web).read()
    soup = BeautifulSoup(html,'html.parser')
    found = []
    tags = soup("a")
    for tag in tags:
        if tag.get("href",None) is not None:
            found.append(tag["href"])
    if(len(found) > upTo):
        web = found[upTo]
    else: break
    
