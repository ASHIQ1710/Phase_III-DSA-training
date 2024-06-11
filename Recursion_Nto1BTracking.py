def printf(i,N):
    if i>N:
        return
    printf(i+1,N)
    print(i)
    return
printf(1,5)