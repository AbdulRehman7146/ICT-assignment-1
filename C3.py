def decimal_to_binary(n):
    if n == 0:
        return "0"
        
    binary_str = ""
    while n > 0:
        remainder = n % 2    
        binary_str = str(remainder) + binary_str  
        n = n // 2                      
    return binary_str
        
print("decimal to binary(10) -> ",decimal_to_binary(10))  
print("decimal to binary(25) -> ", decimal_to_binary(25))