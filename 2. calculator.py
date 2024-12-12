def calculator(a,b,op):
    ans = 0
    
    if op == "add":
        return a + b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
        
    return ans

print(calculator(4,5,"multiply"))
      
    