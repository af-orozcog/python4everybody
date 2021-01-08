#final work of the course

largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done" : break
        num = int(num)
        if largest is None:
            largest = num
            smallest = num
        elif largest < num:
            largest = num
        elif smallest > num:
            smallest = num
    except:
        print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)

