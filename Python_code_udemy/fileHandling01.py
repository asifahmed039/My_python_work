#File Handling
"""
    file access:
        [01]Read
        [02]Write
        [03]Append
    open(),read(),close()
    
"""
file=open('data.txt','r')
data=file.read()
print(data)
file.close()
