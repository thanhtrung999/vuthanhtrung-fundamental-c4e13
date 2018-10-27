items = ['bánh gà','phở','cơm','rau sạch']
print(items)
new_item = input('you want to add:')
items.append(new_item)
print(*items,sep=',')
i = int(input('mời nhập vị trí muốn sửa:'))
new_value = input('tên món mới:')
items[i]=new_value
print(*items,sep=',')
a = int(input('vị trí bạn muốn xóa:'))
items.pop(a)
print(*items,sep=',')
