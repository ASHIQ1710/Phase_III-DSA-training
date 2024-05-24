#Bubble-Sort

def bubble_sort(arr):
    n = len(arr)
    fixThisPosition=n-1
    while fixThisPosition>0:
        for i in range(fixThisPosition):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        fixThisPosition=fixThisPosition-1

arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array is: ",arr)
bubble_sort(arr)
print("Sorted array is: ",arr)
