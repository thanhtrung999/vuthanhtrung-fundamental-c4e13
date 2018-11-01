dicc = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf'],

}
dicc['pocket'] = ["seashell", "strangeberry", "lint"]
print(dicc)
dicc["backpack"].remove("dagger")
print(dicc)
dicc["gold"] += 50
print(dicc)

dicc2 ={
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for i in dicc2:
    print(i)
    print("price: ", dicc2[i])
    print("stock: ", stock[i])
total = 0
for food in dicc2:
    ss = dicc2[food]*stock[food]
    total += ss
print(total)
