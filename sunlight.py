l1=[2,3,4,3,5,4,3,6]
r=[]
for i in range (1,len(l1)):
    if l1[i]>l1[i-1]:
        r.append(l1[i])
print(len(r))
    
