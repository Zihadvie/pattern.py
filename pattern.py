n=int(input("Enter a number who you want to crate tringle patern  : "))
k=0
r=0
while(n!=0):
    k=n%10

    n=n//10
    r=r*10+k
    print(r)
