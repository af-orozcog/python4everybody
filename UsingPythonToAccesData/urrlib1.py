#python app to scan through the web looking for certain patterns

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

address = input("Type the web page address: ")

html = urllib.request.urlopen(address).read()
soup = BeautifulSoup(html,"html.parser")

tags = soup("span")
answer = 0
count = 0
for tag in tags:
    count += 1
    answer += int(tag.contents[0])

print("Count:",count,"Sum:",answer)
