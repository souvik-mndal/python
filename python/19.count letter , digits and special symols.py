inp = input("Enter the word : ")

character,digit,special = (0,0,0)

for ch in inp:
    if( ch.isalpha() ):
        character+=1
    elif( ch.isdigit() ):
        digit+=1
    else:
        special+=1
    

print(f"Character : {character}")
print(f"Digit : {digit}")
print(f"Special Character : {special}")