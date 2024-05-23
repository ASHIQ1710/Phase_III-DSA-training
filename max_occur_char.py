#return character which occuring maximum time with in te given string(if that is tie then print left most character that occurs in alphabetic order)

def reccurent_str(s):
    freq = {}
    count = 0
    ans = ''
    for char in s:
        if char in freq.keys():
            freq[char] += 1
        else:
            freq[char] = 1
        
        if count < freq[char]:
            ans = char
            count = freq[char]
    return ans
        
s = input()
print(reccurent_str(s))

#https://pastebin.com/B0aQ3dYw


word = input()
store = {}
for ch in word:
    if ch in store:
        store[ch] += 1 
    else:
        store[ch] = 1 
 
print(store)
print(store.keys())
 
resultChar = ''
resultFreq = 0
for key in store.keys():
    if resultFreq < store[key]:
        resultFreq = store[key]
        resultChar = key 
    elif resultFreq == store[key] and ord(key) < ord(resultChar):
        resultChar = key
 
print(resultChar)