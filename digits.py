while True:
    n=int(input("Enter a number: "))
    digit=0
    if n>0:
        while n>0:
            n=n//10
            digit=digit+1
        print("The total number of digits are: ", digit)

    elif n<0:
        n=n*-1
        while n>0:
            n=n//10
            digit=digit+1
        print("The total number of digits are: ", digit)

    else:
        print("The number is 0")

