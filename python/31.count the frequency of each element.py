lst = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5]

dict = {}

for i in lst:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)