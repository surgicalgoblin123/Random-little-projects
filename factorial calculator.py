#factorial

def factorial():
    try: 
        x = int(input("Enter an integer: "))
    
    except ValueError:
        print("Enter a valid integer")

    def valid(x):
        return x >= 0
    
    def computation(x):

        if not valid(x):
            return "cannot be less than 0"
        
        if x == 0 or x == 1:
            return 1
        
        return x * computation(x-1)
    
    return computation(x)
    
print(factorial())
