with open("style.txt","r+") as f:
    data=f.read()
    print(data)
    new_data=data.replace("haryana","delhi")
    # f.write(new_data)
    print(new_data)

file=open("style.txt","w")
file.write(new_data)
file.close()