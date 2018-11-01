s = [5,7,300,90,24,50,75]
print('hello, my name is trung and these are my sheep sizes',s)
for cc in range(4):
    smax = max(s)
    print('Now my biggest sheep has sizes',smax)
    a = s.index(smax)
    s[a] = 8
    print('after shearing , here my flock:',s)
    for i in range(len(s)):
        s[i] += 50
    print(s)
total = 0
for t in s:
    total  += t
print('My flock has size in total:',total)
print("I would get:", total, "* 2$ =", total * 2, "$")