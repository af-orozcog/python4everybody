#trying flow of control

score = float(input("Enter Score:"))

if score < 0.0 or score > 1.0:
	print("wrong scale")
elif score < 0.6:
	print("F")
elif score < 0.7:
	print("D")
elif score < 0.8:
	print("C")
elif score < 0.9:
	print("B")
else:
	print("A")
