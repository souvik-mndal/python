n = int(input("Enter the number : "))

for i in range (2,n):
    if(n%i==0):
        print(f"the number {n} is not a prime number")
        break
else:
    print(f"the number {n} is a prime number")