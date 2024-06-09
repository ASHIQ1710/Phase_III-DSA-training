def printBinaryNumber(size, result, n):
    if size == n:
        print(result)
        return
    printBinaryNumber(size + 1, result + "0", n)
    printBinaryNumber(size + 1, result + "1", n)

n = 6
printBinaryNumber(0, "", n)