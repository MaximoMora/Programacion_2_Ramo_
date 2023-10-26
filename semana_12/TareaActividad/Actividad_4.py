



def SumRecursive(n):

    if n <= 0:
        return 1
    else:
        return n + SumRecursive(n-1)

result = SumRecursive(5)
print(result)