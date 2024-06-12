# Un arreglo (array) en si en programacion es un conjunto de informacion
# En python a los arreglos se los conoce como listas
# Una lista es un conjunto de informacion guardada en una variable.

# 1) Una lista se define con corchetes []

# Defino una lista vacia
lista_de_edades = []
# lista_edades_c = [0,0,0,0,0] # EJEMPLO PARA LENGUAJE C (Hay que precargar elementos en las listas)

# Defino una lista con datos precargados
lista_de_edades_precargadas = [20,30,40,15,38] # El indice de una lista va desde el 0 (en este caso el numero 20 tiene un valor de indice de 0) hasta la cantidad de elementos cargados - 1
print(type(lista_de_edades_precargadas))

# 2) Acceder a los elementos de la lista
# 2,1) Accede a un elemento especifico de la lista (en este caso el indicie 2 que seria el numero 40)
# Para eso  es
print(lista_de_edades_precargadas[2])

# 2.2 Imprimir todos los elementos de la lista y de una manera prolija (NUNCA IMPRIMIR LA LISTA COMPLETA)

# FORMA NO RECOMENDADA (NO PODEMOS DEDUCIR LA CANTIDAD DE ELEMENTOS)
for i in range(5) :
    print(f"Edad: {lista_de_edades_precargadas[i]}")

print(len(lista_de_edades_precargadas))

# UNA FORMA RECOMENDADA (SIRVE EN TODOS LOS LENGUAJES) (USANDO EL LEN)
for i in range(len(lista_de_edades_precargadas)) :
    print(f"Edad: {lista_de_edades_precargadas[i]}")

print(len(lista_de_edades_precargadas))

# OTRA FORMA (Usando foreach) aunque en python no se llama asi pero en los demas lenguajes si

for edad in lista_de_edades_precargadas : # Recorre elemento por elemento de una lista y lo guarda en la variable auxiliar edad
    print(f"Edad: {edad}")

# 3) Carga secuencial
# Es una carga ordenada de datos (se va a ir agregando un nuevo dato a la lista luego del ultimo dato agregado)

# 3.1 Carga de un dato
edad = int(input("Ingrese una edad a agregar: "))
lista_de_edades_precargadas.append(edad) # En la mayoria de lenguajes se usa .push)

# 3.1) Carga de varios datos (por ejemplo 5 datos)
# For para pedir los datos
for i in range(5) :
    edad = int(input("Ingrese una edad a agregar: "))
    lista_de_edades.append(edad)

# For para mostrar
for i in range(len(lista_de_edades)) :
    print(f"Edad: {lista_de_edades[i]}")

# A lo C (Tiene que estar inicializada la lista)
# for i in range(5) :
    # edad = int(input("Ingrese una edad a agregar: "))
    # lista_de_edades[i] = edad

# 4) Carga aleaotoria ( Yo le tengo que pedir el indice al usuario) ( ESTO EN PYTHON NO TIENE SENTIDO)

# En que parte de mi array/lista voy a guardar la informacion
#indice = int(input("Ingrese el indice donde va a guardar el dato: "))

# 4.1) Preguntar si ese espacio esta disponible

# if indice > 0 and indice < len(lista_edades_c) :
#     edad = int(input("Ingrese una edad a agregar: "))
#     lista_edades_c[indice] = edad
# else: 
#     print("Error")

# seguir = "si"
# while (seguir == "si") :
#     indice = int(input("Ingrese el indice donde va a guardar el dato: "))

#     if indice >= 0 and indice < len(lista_edades_c) :
#         if lista_edades_c[indice] == 0 :
#             edad = int(input("Ingrese una edad a agregar: "))
#             lista_edades_c[indice] = edad
#         else :
#             print("Dato ya cargado anteriormente")
#     else: 
#         print("Error, fuera del indice")

#     seguir = input("Quiere seguir? Introducza si o no: ")

# print(lista_edades_c)