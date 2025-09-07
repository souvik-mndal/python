fle = open( '32.file handle.txt' , 'a')
flee = open( '32.file handle.txt' , 'r')

fle.write("hi this is a test sentence" )

print(flee.read())

fle.close()