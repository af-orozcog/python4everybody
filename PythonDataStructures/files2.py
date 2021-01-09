#making more stuff with files

fname = input("Enter file name: ")
fh = open(fname)
su = 0
divi = 0
for line in fh:
    check = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = check.find(".")
    su += float(check[pos-1:])
    divi += 1
print("Average spam confidence:",su/divi)
