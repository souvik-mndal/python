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
avg = age.sum() / len(age)
print(f"the average age of the student are --- {avg}")