'''

1. Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
promedio de todos los números.

'''

# 1)

def calcular_promedio() -> float :
    sumador = 0
    lista = []
    while True :
        numero = int(input("Ingrese un numero o ingrese 0 para terminar: "))
        if numero == 0 :
            break
        lista.append(numero)
        sumador += numero

    promedio = sumador / len(lista)
    return promedio

print(f"El promedio es: {calcular_promedio()}")

#! Otra manera de hacerlo

#! def calcular_promedio(lista:list) -> float :
#!     sumador = 0
#!     for i in range(len(lista)) :
#!         sumador += lista[i]

#!     promedio = sumador / len(lista)
#!     return promedio

#! lista_enteros = []
#! while True :
#!     numero = int(input("Ingrese el numero: "))
#!     lista_enteros.append(numero)
#!     seguir = int(input("Ingrese 0 para seguir o ingrese 1 para finalizar: "))
#!     if seguir == 0 :
#!         continue
#!     elif seguir == 1 :
#!         resultado_promedio = calcular_promedio(lista_enteros)
#!         print(f"El promedio es {resultado_promedio}")
#!         break

'''
2. Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
promedio de los números positivos.

'''
def calcular_promedio_positivos() -> float :
    lista = []
    sumador = 0
    contador_negativos = 0
    while True :
        numero = int(input("Ingrese un numero o ingrese 0 para terminar: "))
        if numero == 0 :
            break
        elif numero < 0 :
            lista.append(numero)
            contador_negativos += 1
        else :
            lista.append(numero)
            sumador += numero
    promedio = sumador / (len(lista) - contador_negativos)
    return promedio

print(f"El promedio de los numeros positivos es: {calcular_promedio_positivos()}")

'''

3. Escribir una función que calcule y retorne el producto de todos los elementos de la lista
que recibe como parámetro.

'''

def calcular_producto() -> int :
    lista = []
    multiplicador = 1
    while True :
        numero = int(input("Introduzca un numero o introduzca 0 para terminar: "))
        if numero == 0 :
            break
        lista.append(numero)
        multiplicador *= numero
    
    producto = multiplicador
    return producto

print(f"El producto de todos los elementos ingresados en la lista es de: {calcular_producto()}")
'''

4. Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
del valor máximo encontrado.

'''

def encontar_posicion_valor_maximo(lista:list) :
    valor_maximo = lista[0]
    posicion_valor_maximo = 0
    for i in range(len(lista)) :
        if lista[i] > valor_maximo :
            valor_maximo = lista[i] 
            posicion_valor_maximo = i
        
    return posicion_valor_maximo

lista = []
while True : 
    numero = int(input("Ingrese un numero, o ingrese 0 para terminar: "))
    if numero == 0 :
        break
    lista.append(numero)
posicion = encontar_posicion_valor_maximo(lista)
print(f"El numero maximo esta en la posicion {posicion} de la lista")

'''
5. Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
posiciones en donde se encuentra el valor máximo hallado.
'''

def encontrar_posiciones_valor_maximo(lista:list) :
    valor_maximo = lista[0]
    maximos = []
    for i in range(len(lista)) :
        if lista[i] > valor_maximo :
            valor_maximo = lista[i] 
            maximos.clear()
            maximos.append(i)
        elif lista[i] == valor_maximo :
            maximos.append(i)
            
    print(f"Las posiciones del numero maximo son {maximos} de la lista")

lista = []
while True : 
    numero = int(input("Ingrese un numero, o ingrese 0 para terminar: "))
    if numero == 0 :
        break
    lista.append(numero)
posicion = encontrar_posiciones_valor_maximo(lista)

'''
6. Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe
reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente
reemplazo y luego retornar la cantidad total de reemplazos realizados.

'''

def reemplazar_nombres(lista: list, nombre_a_reemplazar, reemplazo):
    contador_reemplazos = 0
    for i in range(len(lista)):
        if lista[i] == nombre_a_reemplazar:
            lista[i] = reemplazo
            contador_reemplazos += 1

    return contador_reemplazos

lista = ["A", "B", "C", "B", "D"]
print(reemplazar_nombres(lista, "B", "Z"))
print(lista)