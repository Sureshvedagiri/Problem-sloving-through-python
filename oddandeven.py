list1=list(map(int,input().split()))
l2=list1
odd=[]
even=[]
for i in l2:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
odd.sort()
even.sort()
even.reverse()
res=even+odd
print(res)

        

