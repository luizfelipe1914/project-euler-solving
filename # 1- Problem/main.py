#-*- encoding: UTF-8 -*-

def main():
    index = 0
    sum = 0
    while(index < 1000):
        if(index % 3 == 0 or index % 5 == 0):
            sum+= index
        index+=1
    print(f"The sum of multiples of 3 or 5 below 1000 is {sum}.")

if(__name__ == "__main__"):
    main()