def findMaxInArray(index, arr, n, result):
    if index == n:
        print("Max element is: ", result)
        return
    if arr[index] > result:
        result = arr[index]
    findMaxInArray(index + 1, arr, n, result)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)    
findMaxInArray(0, arr, n, arr[0])
# Output: Max element is:  10

def findMaxInArrayWay2(index, arr, n):
    if index==n-1:
        return arr[index]
    nextMax = findMaxInArrayWay2(index+1, arr, n)
    return arr[index] if arr[index]>nextMax else nextMax

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
n = len(arr)
print(findMaxInArrayWay2(0, arr, n))