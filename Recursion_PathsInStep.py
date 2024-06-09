def findnofpaths(i,n):
    if i==n:
        return 1
    if i>n:
        return 0
    cnt=0
    for j in range(1,n+1):
        cnt+=findnofpaths(i+j,n)
    return cnt

n=int(input())
print(findnofpaths(0,n))