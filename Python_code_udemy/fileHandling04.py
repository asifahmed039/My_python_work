#Sequential access files
"""
 Access Method:-                          file types
    Sequential Access files                 text file
    Random acess files                      binary files

"""
with open('My_python_work\Python_code_udemy\Data.txt','r') as file:
    ch1=file.read(1)
    print(ch1)
    ch2=file.read(3)
    print(ch2)
    ch3=file.read()
    print(ch3)

    """
              -10-9-8-7-6-5-4-3-2-1  [PTR]  reverse
                A B C D E F G H I J
                0 1 2 3 4 5 6 7 8 9  [PTR]   starting
                
    """
