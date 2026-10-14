a = int(input("Enter voltage (V) : "))
b = int(input("Enter resistance (ohm) : "))

if b <= 0 :
   print("invalid resistance")
else :
 current = a/b
 print("Current is = ", current,"A")
 if current <=2 : 
      print("Fuse will blow") 
 else :
      print("Circuit is safe")