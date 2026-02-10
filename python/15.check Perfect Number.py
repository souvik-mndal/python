num = int(input("Enter a number: "))
sum_factors = 0

for i in range(1, num):
    if num % i == 0:
        sum_factors += i

if sum_factors == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
