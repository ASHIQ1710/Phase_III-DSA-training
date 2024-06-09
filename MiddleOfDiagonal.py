import random

def MiddleOfDiagonal(grid,m,n):
    res=[]
    cur=[]
    for i in range(m):
        for j in range(n):
            if i==j:
                cur.append(grid[i][j])
    res.append(cur)
    cur=[]
    for i in range(m):
        for j in range(n):
            if i+j==m-1:
                cur.append(grid[i][j])
    res.append(cur)
    print(res)
    res.sort()
    lonDia=res[-1]
    return lonDia[len(lonDia)//2]


m=int(input())
n=int(input())
grid=[]
for i in range(m):
    cur=[]
    for j in range(n):
        cur.append(random.randint(0,1))
    grid.append(cur)
for i in range(m):
    print(grid[i])
print(MiddleOfDiagonal(grid,m,n))