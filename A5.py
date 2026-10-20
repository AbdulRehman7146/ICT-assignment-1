a = int(input("Enter R1: "))
b = int(input("Enter R2: "))
c = int(input("Enter R3: "))

if a <= b and a <= c :
	smallest = a
elif b <= a and b <= c :
	smallest = b
else :
	smallest = c

if a >= b and a >= c :
	largest = a
elif b >= a and b >= c :
	largest = b
else :
	largest = c
	
print("Smallest", smallest)
print("Largest", largest)
