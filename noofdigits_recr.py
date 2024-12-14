def count(n,c=0):
    if n==0:
        return c
    else:
        return count(n//10,c+1)
n=int(input())
print(count(n))
    
    
    
    
