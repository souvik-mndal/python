dict1 = {1:100,2:200,3:300,4:400}
dict2 = {1:500,2:600,3:700,5:800}

for i in dict2:
    if i in dict1.keys():
        dict1[i] += dict2[i]
    else:
        dict1[i] = dict2[i]

print( dict1)