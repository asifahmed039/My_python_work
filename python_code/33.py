#File i/o in python
"""
    Python can be used to perform operations on a file.(read & write data)
        types of all files
            [01]Text Files:-.txt,.docx,.log etc
            [02]Binary Files:-.mp4,.mov,.png,.jpeg etc..


"""
#Open,Read & closed file:-
"""
    Open,Read & closed file:-

        f=open("file_name","mode")
                sample.txt  r:read mode
                demo.docx   w:write mode

        data=f.read()
        f.close()


"""
file=open("demo.txt","w+")  #rb for binary file  rt for text file
file.write("hello")
content=file.read(5)     #can't read or read blank space due to culsor movement
print(content)
file.close()

"""
    'r'     open for reading(default)
    'w'     open for writing, truncating the file first
    'x'     create a new file and open it for writing
    'a'     open for writing, appending to the end of the file if it exists
    'b'     binary mode
    't'     text mode(default) 
    '+'     open a disk file for updating (reading and writing)    
"""
#reading a file
"""
    data=f.read()   #reads entire file
    data=f.readline()   #reads one line at a time

       """
f=open("demo2.txt","r")
data=f.read()
print(data)

line1=f.read()
print(line1)

line2=f.readline()
print(line2)

f.close()
#write mode
"""
    f=open("demo.txt","w")

    f.write("demo.txt","a")    #overwrites the entire file

    f=open("demo.txt","a")
    f.write("this ia a new line")   #adds to the file  #add at the end (append)

"""
#write mode
f1=open("demo3.txt","w")
f1.write("hi i'm python developer.")
f1.close()
#append
f2=open("demo3.txt","a")
f2.write(" Asif Ahmed")
f2.close()
#read,readline
f3=open("demo3.txt","r")
data=f3.read()
print(data)
f3.close()
#r+ write+read pointer at start
f4=open("demo4.txt","r+")
f4.write("Mira Bigha")
data=f4.read()
print(data)
f4.close()
#w+
f4=open("demo5.txt","w+")
print(f4.read())
f4.write("Mira Bigha")
data=f4.read()
print(data)
f4.close()
#a+
f4=open("demo6.txt","a+")
f4.write("Mira Bigha")
data=f4.read()
print(data)
f4.close()


