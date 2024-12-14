wt=int(input("enter the weight of watermelon"))
if wt%2!=0:
    print("no")
else:
    x=wt//2
    if x%2==0:
        print(x,x)
    else:
        print(x-1,x+1)
