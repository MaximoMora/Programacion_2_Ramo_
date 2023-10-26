

def SumPositives(n):
    sumNumber = 0
    for i in range(n,2-1,-1):
        print(i)
        if i % 2 == 0:
            sumNumber += i
        else:
            print("error")

    return sumNumber

    print("suma numero ", sumNumber)

result = SumPositives(4)
print("Resultado: ",result)