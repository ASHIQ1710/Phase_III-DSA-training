# Path: Recursive_Sorting/R_SelectionSort.py 
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

nums = [8, 1, 7, 6, 5, 4, 3, 2]
print("Before sorting:", nums)
performSelectionSort(nums, len(nums))
print("After sorting:", nums)