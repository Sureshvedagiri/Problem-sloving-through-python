candi=list(map(int,input().split()))#1,2,1,3,2
age=list(map(int,input().split()))#17,18,21,20,19
n=int(input())
c=[0]*max(candi)
for i in range(n):
    if age[i]>=18:
        c[candi[i]-1]+=1
temp=c.sort(reverse=True)
if temp[0]==temp[1]:
    print(-1)
else:
    print(c.index(temp[0]+1))
