from pathlib import Path
import os

def getAllTheFiles():
    path = Path('')
    item = list(path.rglob('*'))
    for i,itm in enumerate(item):
        print(f"{i+1} --- {itm}")

def createFile():
    getAllTheFiles()
    try:
        
        name = input("Enter the file name you want to create : ")
        p = Path(name)
        if( not p.exists()):
            with open( p , 'w' ) as fl:
                data = input("Give the data you want to add in the file : ")
                fl.write( data )
            
            print("FILE CREATED SUCCESSFULLY")

        else:
            raise ValueError("file already exists")
    except Exception as err:
        print(f"{err}")

def readFile():
    getAllTheFiles()
    try:
        name = input("Enter the file name you want to read : ")
        p = Path(name)
        if( p.exists() and p.is_file()):
            with open( p , 'r' ) as fl:
                print(fl.read())
                
            print("FILE READED SUCCESSFULLY")

        else:
            raise ValueError("file doesn't exists")
    except Exception as err:
        print(f"{err}")

def updateFile():
    getAllTheFiles()
    name = input("Enter the file name : ")
    p = Path(name)
    try:
        if(p.exists() and p.is_file()):
            print("Enter 1 to update the name of a file")
            print("Enter 2 to override the content of a file")
            print("Enter 3 to append the content of a file")
            inp = int(input("Enter your choice : "))
            if ( inp == 1 ):
                newName = input("Tell your new file name : ")
                p.rename(newName)
            elif ( inp == 2 ):
                with open(p,'w') as fl:
                    data = input("Enter the data : ")
                    fl.write(data)
            elif ( inp == 3 ):
                with open(p,'a') as fl:
                    data = input("Enter the data : ")
                    fl.write(data)
            else:
                raise TypeError("You should choose between 1-3 ")
        else:
            raise TypeError("File not found")
    except Exception as err:
        print(f"{err}")
    
def deleteFile():
    getAllTheFiles()
    try:
        name = input("Enter the file name you want to delete : ")
        p = Path(name)
        if( p.exists() and p.is_file()):
            os.remove(name)
                
            print("FILE DELETED SUCCESSFULLY")

        else:
            raise ValueError("file doesn't exists")
    except Exception as err:
        print(f"{err}")

print("Enter 1 to create a file")
print("Enter 2 to read a file")
print("Enter 3 to update a file")
print("Enter 4 to delete a file")

inp = int(input("Enter a number : "))

if ( inp == 1 ):
    createFile()
elif ( inp == 2 ):
    readFile()
elif ( inp == 3 ):
    updateFile()
elif ( inp == 4 ):
    deleteFile()