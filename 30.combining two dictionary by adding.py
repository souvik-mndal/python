d1 = {1:100,2:200,3:300}
d2 = {3:400,5:500,6:600}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
 
print(d1)