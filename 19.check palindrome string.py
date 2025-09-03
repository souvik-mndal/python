n = input("Enter the number : ")
ans = ""
for i in range( len(n)-1 , -1 , -1 ):
    ans += n[i]


if ( n == ans ):
    print(f"{n} is a palindrome string")
else:
    print(f"the string {n} is not a palindrome string")