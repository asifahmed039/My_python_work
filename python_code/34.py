#file i/o with with Syntax.
"""
syntax:-
  with open("file path","mode") as f:
    data=f.read()


"""
with open("demo07.txt","r+") as f:
    data=f.read()
    print(data)
    f.write(" Great India")

#Deleting a File
"""
Using  the os module

Module (like a code library) is a file written by another programmer that generally has a 
functions we can use.
        some module are pre install in python.
        some are not pre install then use pip(package installer for python)
            pip install module name
            pip3 install module name   #according to version 

        import os   #pre install module no need to install
        os.remove(filename)
"""
#delete file
import os
os.remove("demo.txt")

