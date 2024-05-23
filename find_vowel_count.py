#return count of vowels in given string

def find_vowels(s):
    vowels = ['a','e','i','o','u']
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
s = input()
print(find_vowels(s))