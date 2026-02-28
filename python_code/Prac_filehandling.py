str='Mira Bigha'
f=open('file.txt','w')
f.write(str)
f.close()

f=open('file.txt','r')
data=f.read()
print(data)
f.close()