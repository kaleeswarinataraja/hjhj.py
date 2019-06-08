a1=input()
a1=int(a1)
s1=[]
for i in range(0,a1):
    n=input()
    s1.append(n)
a=[]
for i in zip(*s1):
    if i.count(i[0])==len(i):
        a.append(i[0])
    else:
        break
print(''.join(a))
