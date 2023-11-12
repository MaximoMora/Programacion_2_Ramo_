

lista = [1,3,7,2]

for i in range(len(lista)):
    
    for j in range(len(lista)-i-1):
        if lista[j] > lista[j+1]:
            lista[j],lista[j+1] = lista[j+1],lista[j]
            
            
print(lista)



def binary(lista,target):
    low = 0
    high = len(lista)-1
    med = lista[(low+high)//2]
    
    while lista[med] != target:
        med = lista[(low+high)//2]
        
        if lista[med] > target:
            high = med
        else:
            low = med
            
    print("se encontro: ", lista[med],med)
    
    
binary(lista,7)
