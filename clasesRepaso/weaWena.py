

def insertion_sort(elementos):
    for i in range(1, len(elementos)):
        key = elementos[i]
        j = i - 1
        while j >= 0 and key < elementos[j]:
            elementos[j + 1] = elementos[j]
            j -= 1
        elementos[j + 1] = key

# Ejemplo de uso:
elementos = [12, 11, 13, 5, 6]
insertion_sort(elementos)
print("Array ordenado:", elementos)

