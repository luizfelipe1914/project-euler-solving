#!/usr/bin/env python3

def fibonacci(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
   
def main():
    sum = 0
    for x in range(1, 4000001):
        if(fibonacci(x) % 2 == 0):
            sum += fibonacci(x)
    
    
if(__name__ == "__main__"):
    main()