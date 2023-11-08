


def factNumber(n):

    if n <= 1:
        return n 
    else:
        return n * factNumber(n-1)


result = factNumber(5)

print(result)