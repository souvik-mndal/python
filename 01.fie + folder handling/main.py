from pathlib import Path
import os

def see():
    path = Path('')
    items = list(path.rglob("*"))
    for i,items in enumerate(items):
        print(f"{i+1} --- {items}")
    

def one():
    see()
    filename = input("\n\nEnter the file name : ")
    p = Path(filename)
    try:
        if( not(p.exists()) ):
            with open(p,'w') as fl:
                data = input("insert some data : ")
                fl.write(data)
        else:
            raise ValueError("File already exists\n\n")
    except Exception as err:
        print(err)
    else:
        print("file created successfully\n\n")


def two():
    see()
    foldername = input("\n\nEnter the folder name : ")
    p = Path(foldername)
    try:
        if( not(p.exists()) ):
            os.mkdir(p)
        else:
            raise ValueError("Folder already exists\n\n")
    except Exception as err:
        print(err)
    else:
        print("folder created successfully\n\n")

while( 1 ):
    print("choose 1 to create a file")
    print("choose 2 to create a folder")

    choice = int(input("Enter the choice : "))
    if( choice == 1 ):
        one()
    elif( choice == 2 ):
        two()

