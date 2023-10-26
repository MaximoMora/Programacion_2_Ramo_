
import matplotlib.pyplot as plt
import time



import matplotlib.pyplot as plt
import time


def binonnaciRecursive(n):
    start = time.time()
    if n <= 1:
        end = time.time()

        return 1
    else:
        return binonnaciRecursive(n-1) + binonnaciRecursive(n-2)

    operationTime = end - start
    return operationTime

result = binonnaciRecursive(6)
print(f"result recursive: {result}")



def binonnaciDinamic(n):
    nlist = []
    for i in range(n):
        if i <= 0:
            nlist.append(1)
            continue
        else:

            nlist.append(i)
    print(nlist)
    for i in range(2,n):
        nlist[i] = nlist[i-1] + nlist[i-2]

    
    print(nlist)


print(binonnaciDinamic(6))

