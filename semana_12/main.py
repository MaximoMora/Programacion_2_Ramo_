import matplotlib.pyplot as plt


def FibonnacciRecursive(n):

    if n <= 1:
        return n
    else:
        return FibonnacciRecursive(n-1) + FibonnacciRecursive(n-2)
    

resultRecursive = FibonnacciRecursive(5)
print(resultRecursive)