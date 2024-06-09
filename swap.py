# Method 1: Using a temporary variable
def swap_values_method1(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Method 2: Using tuple packing and unpacking
def swap_values_method2(a, b):
    a, b = b, a
    return a, b

# Method 3: Using arithmetic operations
def swap_values_method3(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
# Method 4: Using bitwise XOR
def swap_values_method4(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
