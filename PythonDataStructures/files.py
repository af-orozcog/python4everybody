#using files

fname = input("Enter the name of the file:")
fl = open(fname)
for line in fl:
    show = line.rstrip()
    print(show.upper())
