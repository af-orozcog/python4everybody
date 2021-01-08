#functions module

def computepay(hrs,rate):
	answer = min(40,hrs)*rate
	hrs -= min(40,hrs)
	if hrs > 0:
		rate *= 1.5
	answer += hrs*rate
	return answer;

hrs = int(input("Enter Hours:"))
rate = float(input("Enter rate:"))
print("Pay",computepay(hrs,rate))

