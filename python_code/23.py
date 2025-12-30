#break & continue
"""
Break:Used to terminate the loop when encountered.

continue:terminates execution in the current iteration & continues execution of the loop
with the next iteration.

"""
i=0
while i<=10:
    # i+=1
    if(i%2==1):      #i%2==0 print odd
        # print("hi")
        i+=1
        continue
    print(i)
    i+=1


    