num = int(input("Enter the number : "))

test = num
rev = 0

while(num):
    last = num%10
    rev = (rev * 10) + last
    num//=10

if( test == rev ):
    print(f"the number is a palindrome")
else:
    print(f"the number isn't a palindrome")
