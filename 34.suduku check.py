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

check = True

for i in range( 0,9,3 ):
    for j in range( 0 , 9 , 3 ):
        block = arr[i:i+3 , j:j+3]
        # sblk = np.hsplit(block , 3)
        # main = np.hstack()
        main = block.reshape(1,9)
        sums = np.sum( main , axis=1 )
        if( sums != 45 ):
            check = False
            print("not valid")
            break


col = np.vsplit(arr,9)
colSum = np.sum(col , axis=0)
colcheck = colSum == 45
colSum = colSum[colcheck]


row = np.hsplit(arr,9)
rowSum = np.sum(row , axis=1)
rowcheck = rowSum == 45
rowSum = rowSum[rowcheck]

total = np.hstack((rowSum,colSum))

for i in range(len(total)):
    if ( total[i] != 45):
        check=False
        print( "not valid")
        break



if( check == True ):
    print( " its a valid suduko")