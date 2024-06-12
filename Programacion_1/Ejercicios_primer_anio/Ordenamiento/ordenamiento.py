
# ? Ordenar de mayor a menor
numeros = [5,3,1,9,7]

print(f"Lista antes de ordenar: {numeros}")

for i in range(len(numeros)) :
    for j in range(i + 1, len(numeros)) :
        if numeros[i] < numeros[j] :
            aux = numeros[i]  #! Intercambio
            numeros[i] = numeros[j] #! Intercambio
            numeros[j] = aux #! Intercambio

print(f"Lista despues de ordenar: {numeros}")

#? Para ordenar de menor a mayor es lo mismo solo que cambiando de signo en la condicion

numeros = [5,3,1,9,7]

print(f"Lista antes de ordenar: {numeros}")

for i in range(len(numeros)) :
    for j in range(i + 1, len(numeros)) :
        if numeros[i] > numeros[j] :
            aux = numeros[i]  #! Intercambio
            numeros[i] = numeros[j] #! Intercambio
            numeros[j] = aux #! Intercambio

print(f"Lista despues de ordenar: {numeros}")
