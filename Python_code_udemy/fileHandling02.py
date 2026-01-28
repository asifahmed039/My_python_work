#Mode in file handling
"""
   [Mode]      [Description]

    r:       read from file
    w:       write to a file
    a:       append a file 
    r+:      read and write
    w+:      write and read
    a+:      Append and Read
    x:       Write in a new file only

Binary Mode

    rb:  Read binary file
    wb:  Write a binary file
    ab:  Append a binary file

"""
file=open('dat.txt','w')
"""
when file is open culsor is always at starting line 
the move according to instruction

"""
st='apna college India'
file.write(st)
file.close()

file=open('dat.txt','a')
st=' 122345'
file.write(st)
file.close()

# file=open('dat.txt','x')
# st='34675994'
# file.write(st)  #give error ? discuss
# file.close()

file=open('mydata.txt','w+')
st='ABCDEF'
file.write(st)
file.seek(0,0)
print(file.read())
file.close()