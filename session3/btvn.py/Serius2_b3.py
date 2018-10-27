a = ['T-shirt','Sweater']
print('Welcome to our shop, what do you want (C, R, U, D)?',a)
new_item = input('Enter new items : ')
a.append(new_item)
print(*a,sep='|')
i = int(input('Update position?'))
new_value = (input('New item?'))
a[i] = new_value
print(*a,sep="|")
cl = int(input('Delete position?'))
a.pop(cl)
print(*a,sep="|")
