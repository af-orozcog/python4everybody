name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counter = {}

for line in handle:
    if not line.startswith("From "): continue
    words = line.split()
    hours = words[-2].split(":")[0]
    counter[hours] = counter.get(hours,0)+1

lst = [(k,v) for k,v in counter.items()]
lst.sort()
for h,c in lst:
    print(h,c)
