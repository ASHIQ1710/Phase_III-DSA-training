def RBubbleSort(a,index1,index2):
    n=len(a)
    if index1==n or index2==n:
        return 
    if a[index2] < a[index1]:
        a[index1],a[index2]=a[index2],a[index1]
    return RBubbleSort(a,index1+1,index2+1)


a=[1,4,2,10]
RBubbleSort(a,0,1)
print(a)