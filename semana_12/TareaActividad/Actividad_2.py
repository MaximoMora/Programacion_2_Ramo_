


def LookWays(n,r):


    def Factorial(n):
        if n <= 1:
            return 1
        else:
            return n * Factorial(n-1)

    
    return  Factorial(n) * (Factorial(r)*(Factorial(n-r)))

result = LookWays(5,2)
print("Resultado de LookWays:",result)