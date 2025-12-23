#Create a new file "practice.txt" using python. Add the following data in it:
#Hi everyone
#we are learning file i/o
#using java.
#i like programming in java.

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning file i/o\nusing java.\ni like programming in java.")

#waf that replace all occurrences of "java" with "python" in above file.
#approach to solve read---override---change
with open("practice.txt","r") as f:
    data=f.read()
    new_data=data.replace("java","python")
    print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

#search if the word "learning" exists in the file or not.
word="Learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")
