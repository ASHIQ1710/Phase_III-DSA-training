def RLinearS(a,x,index):
    n=len(a)
    if index>=n:
        return
    if a[index]==x:
        return index
    else:
        return RLinearS(a,x,index+1)

a=[1,8,7,2,6,17]
x=7
pos=RLinearS(a,x,0)
if pos==None:
    print("Element not found")
print("Elment found at index",pos+1)