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
print(f"The shape of the matrix will be --- {data.shape}")

#To get the average age of the student
print(f"the average age of the students are --- {data[:,0].mean()}")

#To extract maths marks from all student 
print(f"extracting all the marks of maths are --- {data[:,1]}")


#To find highest science marks from all student 
print(f"to find the highest science marks is --- {data[:,2].max()}")


# To get the details of the student who scored more than 90 in maths
print(f"to get all the details who got more than 90in maths is --- {data[data[:,1] > 90]}")


#increase maths marks by 5
print(f"increase the marks of math by 5 --- {data[:,1]+5}")


#find how many students are younger than 19
print(f"to find the youngest students then 19 --- {data[data[:,0]<19]}")


#the average marks of each subjects
print(f"the average marks of maths is --- {data[:,1].mean()} and the average marks of math is --- {data[:,2].mean()}")


#get data of student who scored atleast 80 in both the subjects
print(f"the students who scored atleast 80 in both the subjects --- {data[(data[:,1]>80) & (data[:,2]>80)]}")


#replace all science marks less than 75 with 0
data[:,2][data[:,2]<75] = 0 
print(f"replacing all the science marks less than 75 --- {data}")