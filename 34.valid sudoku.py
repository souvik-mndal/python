import numpy as np

arr = np.array([[5,3,4,6,7,8,9,1,2],
                [6,7,2,1,9,5,3,4,8],
                [1,9,8,3,4,2,5,6,7],

                [8,5,9,7,6,1,4,2,3],
                [4,2,6,8,5,3,7,9,1],
                [7,1,3,9,2,4,8,5,6],

                [9,6,1,5,3,7,2,8,4],
                [2,8,7,4,1,9,6,3,5],
                [3,4,5,2,8,6,1,7,9]])

# row = np.vsplit(arr,9)
# col = np.hsplit(arr,9)

col = (np.sum(arr , axis=0))
row = (np.sum(arr , axis=1))

bool_row = col == 45
bool_col = row == 45

total = np.hstack((col[bool_col] , row[bool_row]))

for i in range( len(total) ):
    if( total[i] != 45 ):
        print("Not valid")
        break
else:
    print("valid ")

