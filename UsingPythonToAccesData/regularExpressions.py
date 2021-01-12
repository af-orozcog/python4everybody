#homework
import re
fl = input("Please write the name of the file: ")
handle = open(fl)

archive = handle.read()
numbers = re.findall("[0-9]+",archive)
ans = 0
for number in numbers:
    ans += int(number)

print("The sum of the numbers is",ans)