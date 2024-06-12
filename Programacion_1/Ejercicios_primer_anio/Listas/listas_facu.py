# # Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el
# # promedio de todos los números.
# def calcular_promedio_lista(lista: list)-> float:
#     acumulador_numeros = 0
#     for i in range(len(lista)):
#         acumulador_numeros += lista[i]
        
#     promedio = acumulador_numeros / len(lista)
#     return promedio

# # lista_enteros = [10, 20, 30, 20, 5, 2, 3, 80] #21.25 es el promedio
# # print(calcular_promedio_lista(lista_enteros))

# # Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el
# # promedio de los números positivos.
# def calcular_promedio_positivos(lista: list)-> float:
#     acumulador_positivos = 0
#     contador_positivos = 0
#     for i in range(len(lista)):
#         if lista[i] > 0:
#             acumulador_positivos += lista[i]
#             contador_positivos += 1
        
#     promedio = acumulador_positivos / contador_positivos
#     return promedio

# # lista_enteros_positivos = [-2, -4, -1, -4, 0, 2, 3, 10, 20] #7 es el promedio
# # print(calcular_promedio_positivos(lista_enteros_positivos))

# # Escribir una función que calcule y retorne el producto de todos los elementos de la lista
# # que recibe como parámetro.
# def calcular_producto_de_lista(lista: list):
#     producto = 1
#     for i in range(len(lista)):
#         producto = producto * lista[i]

#     return producto

# lista_producto = [2, 4, 5, 8, 10, 4] #12800 resultado
# print(calcular_producto_de_lista(lista_producto))

# Escribir una función que reciba como parámetros una lista de enteros y retorne la posición
# del valor máximo encontrado.
def retornar_valor_maximo_lista(lista: list):
    valor_maximo = lista[0]
    posicion_maximo = 0
    for i in range(len(lista)):
        if lista[i] > valor_maximo:
            valor_maximo = lista[i]
            posicion_maximo = i

    return posicion_maximo

lista_maximo = [110, 20, 30, 20, 110, 2, 3, 80, 5]
print(retornar_valor_maximo_lista(lista_maximo))

# Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
# posiciones en donde se encuentra el valor máximo hallado.
# def hallar_posiciones_maximos(lista: list):
#     valor_maximo = lista[0]
#     maximos = []
#     for i in range(len(lista)):
#         if lista[i] > valor_maximo:
#             valor_maximo = lista[i]
#             maximos.clear()
#             maximos.append(i)
#         elif lista[i] == valor_maximo:
#             maximos.append(i)

#     print(maximos)

# # lista = [10, 20, 20, 30]
# # hallar_posiciones_maximos(lista)

# # Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
# # de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe
# # reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente
# # reemplazo y luego retornar la cantidad total de reemplazos realizados.
def reemplazar_nombres(lista: list, nombre_a_reemplazar, reemplazo):
    contador_reemplazos = 0
    for i in range(len(lista)):
        if lista[i] == nombre_a_reemplazar:
            lista[i] = reemplazo
            contador_reemplazos += 1

    return contador_reemplazos

lista_nombres = ["A", "B", "C", "B", "D"]
print(reemplazar_nombres(lista_nombres, "B", "Z"))
print(lista_nombres)