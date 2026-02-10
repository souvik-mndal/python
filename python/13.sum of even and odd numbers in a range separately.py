start = int(input("Enter range start: "))
end = int(input("Enter range end: "))

even_sum = 0
odd_sum = 0

for i in range(start, end + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Even : ",even_sum)
print("Odd : ",odd_sum)
