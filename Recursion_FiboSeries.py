# def fibonacirecursion(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacirecursion(n-1) + fibonacirecursion(n-2)
# n=int(input())
# print(fibonacirecursion(n))
# # Time Complexity: O(2^n)

# Using Memoization 
def findNthTermUsingCache(n, cache):
    if n == 1 or n == 2:
        return 1 
    elif cache[n] != -1:
        return cache[n]
    result1 = findNthTermUsingCache(n - 1, cache)
    result2 = findNthTermUsingCache(n - 2, cache)
    cache[n] = result1 + result2
    return result1 + result2 
#Time Complexity: O(n)
 
# Tabulation approach (Ultimate Dynamic programming solution)
def findNthTermUsingTabulation(n):
    cache = [-1] * (n + 1)
    # Whatever base condition we wrote 
    # recursive solutin, we need to 
    # initialize them here
    cache[1] = 1 
    cache[2] = 1 
    # 1 - wherever 'n' is present, replace it with index 
    # 2 - wherever 'functionCall' is there replace it with cache 
    for index in range(3, n + 1):
        result1 = cache[index - 1]
        result2 = cache[index - 2]
        cache[index] = result1 + result2
 
    return cache[n]
#Time Complexity: O(n)
    

n=int(input())
cache = [-1] * (n + 1)
print(findNthTermUsingCache(n, cache)) # Using Memoization
print(findNthTermUsingTabulation(n)) # Using Tabulation