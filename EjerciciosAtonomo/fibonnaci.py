

def Fibonnaci(n):

    if n <= 1:
        return n 
    else:
        return Fibonnaci(n-2) + Fibonnaci(n-1)


result = Fibonnaci(6)
print(result)