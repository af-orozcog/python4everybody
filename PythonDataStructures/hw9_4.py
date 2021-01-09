#assigment 9.4

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counter = {}
for line in handle:
    if not line.startswith("From "):continue 
    words = line.split()
    counter[words[1]] = counter.get(words[1],0)+1

co = 0

for word,coun in counter.items():
    if coun > co:
        answer = word
        co = coun
print(answer,co)