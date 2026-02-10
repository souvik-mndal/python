num = int(input("Enter the number : "))

rev = 0

while(num):
    last = num%10
    rev = (rev * 10) + last
    num//=10

print(f"the reverse of the given number is : {rev}")