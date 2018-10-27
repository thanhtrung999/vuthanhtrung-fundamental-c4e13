a = input('hi there , this is a superuser gateway username: ')
if not  a == 'c4e':
     print('you are not superuser')
else:
    s =  input('passwword:')
    while True:
        
        if not s == 'codethechange':
            print('passwword is incorrect')
            s =  input('passwword:')
        else:
            print('welcome,c4e')
            break