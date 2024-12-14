l1=list(map(int,input().split()))
l1.sort()
sums=0
for i in range(0,3):
    sums=sums+l1[i]
print(sums)
    
