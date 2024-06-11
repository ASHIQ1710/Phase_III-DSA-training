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
 
def performBubbleSort(nums, n):
    if n == 1:
        return 
 
    # last index is (n - 1)
    for index in range(n - 1):
        if nums[index] > nums[index + 1]:
            nums[index], nums[index + 1] = nums[index + 1], nums[index]
 
    performBubbleSort(nums, n - 1)    
 
 
def performSelectionSort(nums, n):
    if n == 1:
        return 
 
    # fix (n-1)th index 
    maxEleIndex = n - 1 
    for index in range(n - 1):
        if nums[index] > nums[maxEleIndex]:
            maxEleIndex = index 
 
    if maxEleIndex != n - 1:
        nums[maxEleIndex], nums[n - 1] = nums[n - 1], nums[maxEleIndex]
 
    performSelectionSort(nums, n - 1)
 
 
 
def performInsertionSort(nums, n):
    if n == 1:
        return 
 
 
    performInsertionSort(nums, n - 1)
    # nums = [1, 3, 4, 5, 6, 7, 8, 2]
    # nums = [1, 3, 3, 4, 5, 6, 7, 8]
    currValue = nums[n - 1]
    prevIndex = n - 2
    while prevIndex >= 0:
        if nums[prevIndex] > currValue:
            nums[prevIndex + 1] = nums[prevIndex]
        else:
            break 
        prevIndex -= 1 
    nums[prevIndex + 1] = currValue
 
 
def performCountingSort(nums, n):
    pass
 
nums = [8, 1, 7, 6, 5, 4, 3, 2]
 
print("Before sorting:", nums)
performInsertionSort(nums, len(nums))
print("After sorting:", nums)