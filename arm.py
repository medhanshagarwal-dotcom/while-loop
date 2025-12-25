n=int(input("Enter a number: "))
p=len(str(n))
l=n
sum=0
while l>0:
    digit=l%10
    sum+=digit**p
    print(sum)
    l//=10

if sum==n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")