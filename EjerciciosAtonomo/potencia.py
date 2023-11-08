


def powerNumber(n,power):

    if power <= 1:
        return 1
    
    else:
        return n * powerNumber(n,power-1)


result = powerNumber(4300,996)
print(result)



