import numpy as np

arr = np.array([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],

                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],

                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]])



rows = np.sum(arr,axis=1)
# print(rows)
cols = np.sum(arr,axis=1)
# print(cols)

block = np.vsplit(arr,3)
for i in range(len(block)):
    blocks = np.hsplit(block[i],3)
    
    # print( blocks)
    for j in range(len(blocks)):
        if(blocks[j].sum() != 45 ):
            print("Not a valid suduku")
            break

for i in range(len(rows)):
    if( rows[i] != 45 ):
        print( "Not a valid suduko")
        break


for i in range(len(cols)):
    if( cols[i] != 45 ):
        print( "Not a valid suduko")
        break

print("its a valid suduko")

