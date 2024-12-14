n=input()
e1=''
e2=''
for i in n:
    if n.count(i)>=2 and i not in e1:
        e1=e1+(i*2)
    if n.count(i)==1:
        e2=e2+i
print(e1+e2)
