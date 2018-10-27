s = input('nhập passwword : ')

while True:
    
    if len(s)<=8:
        print('độ dài lơn hơn 8')
    elif s.isalpha():
        print('phải có số')
    elif s.islower() or s.isupper() or s.isdigit() or s.isnumeric():
        print('phải có chữ in hoa và thường')
    else:
        break
    s = input('nhập passwword : ')



        
    

    
