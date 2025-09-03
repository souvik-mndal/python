n = input("Enter the number : ")
ans = ""
for i in range( len(n)-1 , -1 , -1 ):
    ans += n[i]

print(f"reversed - {ans}")