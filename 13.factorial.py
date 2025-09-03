n = int(input("Enter the number : "))
ans=1
for i in range (1,n+1):
    ans *= i

print(f"The factorial of the number {n} is {ans}")