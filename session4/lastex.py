b1 = [
    {
        'no':1,
        'name':'huy',
        'hours':30,
        'vnd':50,
    },
    {
        'no':2,
        'name':'quan',
        'hours':20,
        'vnd':40,
    },
    {
        'no':3,
        'name':'duc',
        'hours':15,
        'vnd':35,
    }
]
c = 0
for i in b1:
    print(i['hours'])

for k in b1:
    print(k['vnd']*k['hours'])
    c += k['vnd']*k['hours']
    
print(c)