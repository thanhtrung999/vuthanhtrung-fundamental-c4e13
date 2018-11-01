dicc = {
    'person':'con người',
    'home': 'nhà',
    'hw': 'bài tập',
    'list': 'danh sách',
}

while True:
    for i in dicc:
        print(i , end=' ')
    print()
    a = input('your code?')

    if a in dicc:
      print(dicc[a])
    else:
        b = input('not found,do you want to contribute this word?(y/n)')
        print(b)
        if b =='y':
            c = input('nhập thêm key mới:')
            d = input('ý nghĩa của key mới')
            dicc[c] = d
        else:
            print("cảm ơn , quay lại với từ điển")
        

