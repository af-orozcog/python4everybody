#python program to read through a xml file

import urllib.request,urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter the web page URL: ")

print("retriving data from:",url)

xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)

lines = tree.find("comments")
lines = lines.findall("comment")
count = 0
answer = 0
for obj in lines:
    check = obj.findall("count")
    for val in check:
        count += 1
        answer += int(val.text)
print("Count is",count,"the sum is",answer)