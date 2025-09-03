n = int(input("Enter the number : "))

odd,even = 0,0

for i in range (1,n+1):
    if (i%2 == 0):
        even+=i
    else:
        odd+=i

print(f"the total sum of odd number is : {odd} \n the total sum of even number is : {even}")
    