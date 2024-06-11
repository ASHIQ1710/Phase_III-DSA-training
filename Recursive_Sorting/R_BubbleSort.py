def recursiveBubbleSort(arr, n):
    if n == 1:
        return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    recursiveBubbleSort(arr, n-1)

a=[1,4,2,10,23,3,1,0,20,11,12,13,14,15,16,17,18,19,5,6,7,8,9,22,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
recursiveBubbleSort(a, len(a))
print(a)
 