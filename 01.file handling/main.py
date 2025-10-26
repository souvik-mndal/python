from pathlib import Path
import os

def see():
    path = Path("")
    items = list(path.glob("*"))
    for i,items in enumerate(items):
        print(f"{i+1} --- {items}")




def creation():
    see()
    name = input("give me the file name : ")
    p = Path(name)
    try:
        if( p.exists() ):
            raise ValueError("this file already exists")
        with open(p,'a') as fl:
            data = input("enter some data in the file : ")
            fl.write(data)
    except Exception as err:
        print(err)
    else:
        print("file created successfully")


def reading():
    see()
    name = input("give me the file name : ")
    p = Path(name)
    try:
        if( not p.exists() ):
            raise ValueError("this file doesn't exists")
        if( p.exists() and p.is_file() ):
            with open(p,'r') as fl:
                print( fl.read() )
    except Exception as err:
        print(err)
    else:
        print("file read successfully")


def updating():
    see()
    print("choose 1 to update the file name : ")
    print("choose 2 to override the file data : ")
    print("choose 3 to append the file data : ")
    choose = int(input("enter the choice : "))
    if( choose == 1 ):
        name = input("give me the file name : ")
        newname = input("give me the new file name : ")
        p = Path(name)
        pp = Path(newname)
    
    
        try:
            if( not p.exists() ):
                raise ValueError("this file doesn't exists")
            if( p.exists() and p.is_file() ):
                p.rename(pp)
        except Exception as err:
            print(err)
        else:
            print("file name updated successfully")
    if( choose == 2 ):
        name = input("give me the file name : ")
        p = Path(name)
    
    
        try:
            if( not p.exists() ):
                raise ValueError("this file doesn't exists")
            if( p.exists() and p.is_file() ):
                with open(p,'w') as fl:
                    data = input("Enter the data : ")
                    fl.write(data)
        except Exception as err:
            print(err)
        else:
            print("file updated successfully")
    if( choose == 3 ):
        name = input("give me the file name : ")
        p = Path(name)
    
    
        try:
            if( not p.exists() ):
                raise ValueError("this file doesn't exists")
            if( p.exists() and p.is_file() ):
                with open(p,'a') as fl:
                    data = input("Enter the data : ")
                    fl.write(data)
        except Exception as err:
            print(err)
        else:
            print("file updated successfully")




def removing():
    see()
    name = input("give me the file name : ")
    p = Path(name)
    try:
        if( not p.exists() ):
            raise ValueError("this file doesn't exists")
        if( p.exists() and p.is_file() ):
            os.remove(p)
    except Exception as err:
        print(err)
    else:
        print("file removed successfully")




while (True):
    print("choose 1 to create a file ")
    print("choose 2 to read a file ")
    print("choose 3 to update a file ")
    print("choose 4 to delete a file ")
    print("choose 5 to exit ")

    choose = int( input ( "Enter the number : "))
    if( choose == 1 ):
        creation()
    elif ( choose == 2 ):
        reading()
    elif ( choose == 3 ):
        updating()
    elif ( choose == 4 ):
        removing()
    else:
        break