n = input("Enter anything : ")

digit,char,symbol = 0,0,0

for i in range(0,len(n)):
    if( n[i].isdigit() ):
        digit+=1
    elif (n[i].isalpha()):
        char+=1
    else:
        symbol+=1

print(f"numbers : {digit}\nalphabet : {char} \n symbols : {symbol}")