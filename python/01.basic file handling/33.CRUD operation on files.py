from pathlib import Path
import os

def readFiles():
    path = Path('')
    item = list(path.rglob("*"))

    for i,item in enumerate(item):
        print(i+1,item)

def createFile():
    readFiles()
    try:
        fileName = input("Enter the name of the file : ")
        p = Path(fileName)
        if( not p.exists() ):
            with open(p,"w") as fl:
                inp = input("Add something : ")
                inp += " "
                fl.write(inp)
        else:
            raise ValueError("File already exists")
    except Exception as err:
        print("Error occoured ",err)
    else:
        print("File created successfully")
    
        
def readFile():
    readFiles()
    try:
        fileName = input("Enter the name of the file : ")
        p = Path(fileName)
        if( p.exists() ):
            with open(p,"r") as fl:
                print(fl.read())
        else:
            raise ValueError("File doesn't exists")
    except Exception as err:
        print("Error occoured ",err)
    else:
        print("File readed successfully")

def updateFile():
    readFiles()
    try:
        fileName = input("Enter the name of the file : ")
        p = Path(fileName)
        if( p.exists() ):
            with open(p,"a") as fl:
                inp = input("Add something : ")
                fl.write(inp)
        else:
            raise ValueError("File doesn't exists")
    except Exception as err:
        print("Error occoured ",err)
    else:
        print("File updated successfully")
    

def deleteFile():
    readFiles()
    try:
        fileName = input("Enter the name of the file : ")
        p = Path(fileName)
        if( p.exists() ):
            os.remove(p)
        else:
            raise ValueError("File doesn't exists")
    except Exception as err:
        print("Error occoured ",err)
    else:
        print("File removed successfully")
    

while(True):
    print("Enter 1 to create a file")
    print("Enter 2 to read a file")
    print("Enter 3 to update a file")
    print("Enter 4 to delete a file")
    print("Enter 5 to exit ")

    ans = int(input("Enter the choice : "))
    if( ans == 1 ):
        createFile()
    if( ans == 2 ):
        readFile()
    if( ans == 3 ):
        updateFile()
    if( ans == 4 ):
        deleteFile()
    if( ans == 5 ):
        break