dict1 = {1:100,2:200,3:300,4:400}
dict2 = {5:500,6:600,7:700,8:800}

for i in dict2:
    dict1.update({i:dict2[i]})

print(dict1)