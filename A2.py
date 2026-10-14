a = int(input("Enter the value of current :"))
if a == 0 :
	print("No current flow")
elif a <= 0 :
	print("Current flows from A to B")
else :
	print("Current flows from B to A")