def R_BinaryS(a,x,low,high):
    if low > high:
        return -1
    n=len(a)
    mid=(low+high)//2
    if mid> n or mid<0:
        return -1
    if a[mid]==x:
        return mid
    if a[mid] > x:
        return R_BinaryS(a,x,low,mid-1)
    elif a[mid]<x:
        return R_BinaryS(a,x,mid+1,high)


a=[1,23,44,55,66]
x=48
n=len(a)
pos=R_BinaryS(a,x,0,n-1)
if pos ==-1:
    print("Not Found")
else:
    print("elemnt found at pos ",pos+1)