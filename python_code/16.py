 #Dictionary in python
"""
Dictionaries are used to store data values in key:values pairs
they are unordered mutable (changable) & do not allow duplicate keys
   #key unique 

syntax
access dic["name"],dic["marks"]
add new dic["key"]="value"

"""
            #code
dic={
    "name":"sunny",
    "subject":["maths","c++","python"],
    "topics":("dictionary","list","tuple"),
    "age":26,
    "is_adult":True,
    12.4:"wifi"    #tuple and strings are not allowed as keys because of immutable nature.
}
print(dic)
print(type(dic))  #type 
print(dic["name"])   #access values from dic
print(dic["topics"])
print(dic[12.4])

dic["name"]="Asif"
#adding new key and value pair
dic["sur_name"]="Ahmed"
print(dic)

#null dictionary
null_info={

}

null_info["name"]="Mr Rehan"
print(null_info)


