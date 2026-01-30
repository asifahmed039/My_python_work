#Random Access files
"""
   [01] seek(offset,where)
   [02] tell()   its give current position of culsor
"""

with open('My_python_work\Python_code_udemy\Data.txt','rb') as file:
    print(file.read(4))
    print(file.tell())

    file.seek(3,0)
    print(file.read(2))
