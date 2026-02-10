size = int(input("Enter the size : "))

lst = []

for i in range(0,size):
    inp = int(input(""))
    lst.append(inp)

maxi = lst[0]
index = 0

for i,item in enumerate(lst):
    if( maxi < item ):
        maxi = item
        index = i

print(f"The greatest number is : {maxi} at index : {index}")