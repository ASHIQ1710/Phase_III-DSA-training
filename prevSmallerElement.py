from collections import deque

def get_previous_smaller_element(queue):
    result = []
    stack = []

    # Iterate through the queue
    while queue:
        current_element = queue.popleft()

        # Find the previous smaller element
        while stack and stack[-1] >= current_element:
            stack.pop()

        # Add the previous smaller element to the result list
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

        # Push the current element to the stack
        stack.append(current_element)

    return result

# Example usage
queue = deque([4, 5, 2, 10, 8])
result = get_previous_smaller_element(queue)
print(result)