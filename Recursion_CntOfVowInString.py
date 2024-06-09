def countVowels(s):
    vowels = "aeiou"
    if s == "":
        return 0
    if s[0].lower() in vowels:
        return 1 + countVowels(s[1:])
    else:
        return countVowels(s[1:])
s="Hello"
print(countVowels(s)) # Output: 2

def countVowelsWay1(word, index, n, result):
    if index == n:
        print("Vowels count is:", result)
        return 
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        result += 1 
    countVowelsWay1(word, index + 1, n, result)
 
 
word = "abcdeefuigh"
countVowelsWay1(word, 0, len(word), 0)
 
 
 
 
def countVowelsWay2(word, index, n):
    if index == n:
        return 0 
    nextVowelsCount = countVowelsWay2(word, index + 1, n)
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        nextVowelsCount += 1 
    return nextVowelsCount
 
 
word = "abcdeefuigh"
result = countVowelsWay2(word, 0, len(word))
print("Vowels count is:", result)