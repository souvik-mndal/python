import os 
from pathlib import Path

def createFolder():
    inp = input("Enter the folder name : ")
    if( not os.path.exists(inp) ):
        os.mkdir(inp)
    else:
        print("File already exists")

def createFile():
    print("Enter 1 to create a file outside ")
    print("Enter 2 to create a file inside a folder ")
    inp = int(input("Enter the folder name : "))
    
    if( inp == 1 ):
        fle = input("Enter the file name : ")
        p = Path(fle)
        with open( p , 'w' ) as fl:
            data = input("ENter the inner data : ")
            fl.write(data)
    if( inp == 2 ):
        fldr = input("Enter the folder name : ")
        if( os.path.exists(fldr) ):
            fle = input("Enter the file name : ")
            p = Path(fldr) / fle
            if( not p.exists() ):
                with open( p , 'w' ) as fl:
                    data = input("ENter the inner data : ")
                    fl.write(data)
            else:
                print("file already present")



print("Enter 1 to create a folder")    
print("Enter 2 to create a file ")       

inp = int(input("Enter the number : "))

if( inp == 1 ):
    createFolder()
if( inp == 2 ):
    createFile()