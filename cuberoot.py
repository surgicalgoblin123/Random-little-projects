x = 27
guess = 1

def valid(x,guess):
    if x < 0 and guess <= 0:
        return False
    else:
        return x,guess

def check_accuracy():
    result = x,guess
    
    if not result:
        return "Invalid"
    
    number, est = result
    while abs(est**3 - number) >= 0.001:
        est = newton_of_cubic(number,est)
    return est
    

def newton_of_cubic(cube,estimate):
    y = ((cube/(estimate**2)) + (2*estimate)) / 3
    avg = (estimate + y) / 2
    return avg

print(check_accuracy())