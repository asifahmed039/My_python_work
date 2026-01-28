"""
read methods:-            write mehods:             others:
    read()                   write()                readable()
    read(size)              writelines()            writeable()
    readline()              truncate()              close()  
    readlines()

cursor position:
    tell()
    seek(offset,0/1/2)  0 starting  1 from current oposition 2 end position(reverse)

another syntax:
    with open('f_name','mode') as file:
 


"""
file=open('mydata.txt','r')
dt=file.read(3)
file.seek(0,0)
dt=file.readlines()
print(dt)
file.close()


file=open('mydata.txt','w')
dt=['one\n','two\n','three\n','four\n','five\n']
file.writelines(dt)
print(dt)
file.close()