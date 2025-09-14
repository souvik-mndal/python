import numpy as np

# age , math marks , science marks
data = np.array([
    [18, 85, 78],  # Student 1
    [19, 92, 88],  # Student 2
    [17, 76, 95],  # Student 3
    [18, 65, 70],  # Student 4
    [20, 90, 85]   # Student 5
])


#To get the shape of the matrix
print(f"the shape of the matrix is --- {np.shape(data)}")

#To get the average age of the student
age = data[: , 0:1 ]
print(f"the average age of the student are --- {np.mean(age)}")


#To extract maths marks from all student 
math = data[: , 1:2]
print(f"the maths marks for all student are --- {np.vsplit(math,len(math))}")


#To find highest science marks from all student 
science = data[: , 2:]
print(f"the highest science marks for all student are --- {science.max()}")


#To get the details of the student who scored more than 90 in maths
math = data[: , 1:2]
boolcheck = math > 90
for i in range( len(boolcheck) ):
    if( boolcheck[i] ):
        print(f"the data of the student who scored more than 90 in maths are ---\n {data[i]}")


