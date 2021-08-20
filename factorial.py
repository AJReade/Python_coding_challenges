def calcFactorial(n):
    print ("n=",n)
    if n == 0:
        factorial = 1
    else:
        factorial = n * calcFactorial(n-1)
        print("At A",factorial)                     #line A
    return factorial
print(calcFactorial(4))

def factorial(n):
    total = 1
    totals = []
    for i in range(2,n+1):
        total = total * i 
        totals.append(total)
    return total, totals
print(factorial(10))   



