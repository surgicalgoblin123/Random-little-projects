x = int(input("Number to find square root: "))
guess = int(input("Guess the answer: "))

def valid(x,guess):
    if x < 0 or guess <= 0:
        return False
    else:
        return x,guess
    
def check_accuracy():
    result = valid(x,guess)
    
    if not result:
        return "Invalid"
    
    number,est = result
    while abs(est**2 - number) >= 0.001:
        est = newton(number,est)
    return est

def newton(square_root,estimate):
    y = (square_root / estimate)
    new_guess = (estimate + y) / 2
    return new_guess

print(check_accuracy())