a = int(input("Enter A : "))
b = int(input("Enter B : "))

if (a == 0 or a == 1) and (b == 1 or b == 0) :
	or_result = a | b
	and_result = a & b
	xor_result = a ^ b
	print("OR = ", or_result)
	print("And = ", and_result)
	print("XOR = ", xor_result)
else :
	print("Bits must be 0 or 1")
