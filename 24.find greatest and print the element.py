lst = [16,4,1,4,6,658,4,65,6,4,231,5,1,31,35,84,6,6,4,153,48,531,564]

greatest = -1
index = -1

for i in range(0,len(lst)):
    if( lst[i] > greatest ):
        greatest = lst[i]
        index = i

print(f"the greatest element is : {greatest} and the index its lying is : {index}")
