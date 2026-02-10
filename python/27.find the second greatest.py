size = int(input("Enter the size : "))

lst = []

for i in range(0,size):
    inp = int(input(""))
    lst.append(inp)

maxi = lst[0]
sec_maxi = -1

for i,item in enumerate(lst):
    if( maxi < item ):
        sec_maxi = maxi
        maxi = item
    elif( item > sec_maxi ):
        sec_maxi = item

print(f"The second greatest number is : {sec_maxi}")