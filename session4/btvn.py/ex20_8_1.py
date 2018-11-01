a = input('enter data:')
b = 'abcdefghijklmnopqrstuvwxyz'
a = a.lower()
dicc = {}
for char in a:
    if char in b:
        if char in dicc:
            dicc[char] = dicc[char] + 1
        else:
            dicc[char] = 1
keys = dicc.keys()
for char in keys:
    print(char, dicc[char])



