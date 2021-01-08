#conditional statements execersices

hrs = int(input("Enter Hours:"))
rate = float(input("Enter the rate:"))
answer = min(hrs,40)*rate
rate *= 1.5
hrs -= min(hrs,40)
answer += hrs*rate
print(answer)
