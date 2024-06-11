
#path: Recursive_Sorting/R_InsertionSort.py
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