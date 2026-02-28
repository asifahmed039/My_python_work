#Random Access binary files
"""
    Struct module is used to create binary file in python
        struct()  method
            encode()   decode()  
    ex:-
        Players 
            id=14
            name=smith
        file name   players.dat
                  14 Smith
                  16 Varun
                  1 Ravi          #record
                  20 Kiran
                  4 Ali

Formatting 
Integer
format type   size

    h  Short    2
    i  int      4
    I  unsigned int  4
    l  long          8
    L  unsigned long  8

Float
    f  float  4
    d  double  8

String
    s char[]
    p char[]

Character
    c  char             1
    b signed char       1
    B  unsigned char    1
    ?  _Bool            1


"""
import struct
id=14
name='Smith'
Record_size=14
def add_player(id,name):
    with open('players.dat','ab')as file:
        name=name.encode().ljust(10)
        record=struct.pack('i10s',id,name)   #packing the data in binary format
        file.write(record)

index=2
def find(index):
    with open('players.dat','rb') as file:
        file.seek(index*Record_size)
        record=file.read(Record_size)
        if record:
            id,name=struct.unpack('i10s',record)
            print(f'id:{id},name:{name.decode()}')
        else:
            print('no record')



add_player(id,name)
add_player(2,'Ravi')
find(index)




