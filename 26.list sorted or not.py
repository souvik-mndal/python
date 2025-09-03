lst = [1,2,3,4,5,6,7,8,9,10]

ans = True

for i in range(1,len(lst)):
    if( lst[i]<lst[i-1]):
        ans = False
        break

if ( ans ):
    print("the list is sorted in ascending order")
else:
    print("the list is NOT sorted in ascending order")