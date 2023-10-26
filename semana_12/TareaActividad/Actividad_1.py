

def FibonnaciRecursive(n):

    if n <= 1:
        return 1
    else:
        return FibonnaciRecursive(n-1) + FibonnaciRecursive(n-2)


print(FibonnaciRecursive(5))