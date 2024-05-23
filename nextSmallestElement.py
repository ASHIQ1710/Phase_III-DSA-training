from collections import deque

def find_next_greater(arr):
    stack = []
    result = [-1] * len(arr)
    queue = deque()

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]

        stack.append(i)

    for i in range(len(arr)):
        while queue and arr[i] > arr[queue[0]]:
            index = queue.popleft()
            result[index] = arr[i]

        queue.append(i)

    return result

# Example usage
arr = [4, 2, 8, 1, 6, 5, 9]
next_greater = find_next_greater(arr)
print(next_greater)