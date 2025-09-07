lst = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,7,8]

dck = {}

for i in lst:
    if i in dck.keys():
        dck[i] += 1
    else:
        dck[i] = 1

print(dck)