num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))

if(num1 < num2):
    print(f"the greatest number is : {num2}")
elif(num1 == num2):
    print("both the numbers are same")
else:
    print(f"the greatest number is : {num1}")