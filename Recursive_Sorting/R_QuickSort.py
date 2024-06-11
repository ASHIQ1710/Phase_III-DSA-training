def getPivotIndex(nums, left, right):
    pivot = nums[right]
    # [18, 12, 22, 23, 10, 7, 20]
     # [18, 12, 10, 23, 22, 7, 20]
     # [18, 12, 10, 7, 22, 23, 20]
 
 
 
    # [18, 12, 10, 7, 22, 23, 20]
    # [18, 12, 10, 7, 20, 23, 22]
    position = left
    for index in range(left, right):
        if nums[index] < pivot:
            nums[index], nums[position] = nums[position], nums[index]
            position += 1 
 
    nums[right], nums[position] = nums[position], nums[right]
    return position
 
 
 
def findPivotAndSort(nums, left, right):
    if left >= right:
        return 
    pivotIndex = getPivotIndex(nums, left, right)
    findPivotAndSort(nums, left, pivotIndex - 1)
    findPivotAndSort(nums, pivotIndex + 1, right)
 
def performQuickSort(nums):
    n = len(nums)
    findPivotAndSort(nums, 0, n - 1)
 
 
 
 
nums = [8, 1, 7, 6, 5, 4, 3, 2, -1, -2, -3, -100, 100]
 
print("Before sorting:", nums)
performQuickSort(nums)
print("After sorting:", nums)