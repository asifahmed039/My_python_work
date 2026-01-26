#[86]Resetting password
pwd1='Asif@331999'
pwd2='Asif@331999'
if pwd1==pwd2:
    print("password changed")
else:
    if pwd1.casefold()==pwd2.casefold():
        print('please check cases and again')
    else:
        print('password do not match')
