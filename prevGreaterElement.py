from collections import deque

def find_previous_greater_elements(arr):
    result = []
    queue = deque()

    for i in range(len(arr)):
        while queue and queue[-1] <= arr[i]:
            queue.pop()

        if queue:
            result.append(queue[-1])
        else:
            result.append(-1)

        queue.append(arr[i])

    return result

# Example usage
arr = [3, 5, 2, 8, 6, 10, 7, 9]
result = find_previous_greater_elements(arr)
print(result)