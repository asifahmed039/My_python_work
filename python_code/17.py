#Nested dictionay
dict={
    "name":"rahul kumar",
    "subjects":{
        "phy":97,               # nested dictionary
        "chem":98,
        "math":99
    }
}

print(dict["subjects"]["math"])

#methods in dictionary

"""
myDic.keys()   #return all keys
myDic.values() #return all values
myDic.items()  #return all (key,value) pair as tuples
myDic.get("key") #return the key according to value
myDic.update({newdic)  #inserts the specified items to the dictionary

"""
#keys
print(dict.keys())
#typecasting of dic
print(len(list(dict.keys())))
#one more way
print(len(dict))

#values
print(dict.values())
print(list(dict.values()))

#items
pairs=list(dict.items())
print(pairs[0])

#gets
print(dict["name"])
print(dict.get("name"))   #best to use for access values from dic

#update
dict.update({"city":"Patna"})
print(dict)

new_dic={"language":"hindi" ,"name":"Rehan Alam"}   #over writing
dict.update(new_dic)
print(dict)
