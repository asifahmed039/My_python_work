#Binary vs Text files
"""
    Text file:-
            only perform sequential access 

            data.txt (human readable)    cat Data.txt in terminal
    Binary file:-
            sequential as well as random accessd 

            logo.png file  (logo of python)  binary data (not human readable )

            cat python.png (terminal)

"""
i=10
s='hello'
with open('DData.txt','wb') as file:
    file.write(i)  #its give error not string
    file.write(s)


