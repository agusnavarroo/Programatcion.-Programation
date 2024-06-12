'''

Listas simples:
1- Realizar una función que ordene una lista de entero en orden ascendente o
descendente dependiendo de un parámetro que se le envíe, la función debe retornar
la cantidad de cambios que se realizaron.
2- Realizar una función que ordene una lista de nombres de la A-Z o viceversa
dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad
de cambios que se realizaron.
3- Similar a la función anterior, se debe realizar otra que ordene una lista de
nombres por su largo, de manera ascendente o descendente, la función debe
retornar la cantidad de cambios que se realizaron
Matrices:
4- Ordenar una matriz de nombre-apellido de la A-Z o viceversa dependiendo de un
parámetro que se le envíe, por otro lado, la función deberá recibir otro parámetro
para indicar si la prioridad de ordenamiento la tendrá el nombre o el apellido

'''

while True :
    opcion_funcion = int(input("Ingrese 1 para ordenar numeros, ingrese 2 para ordenar nombres, ingrese 3 para ordenar una lista de nombres por su largo, 4 para ordenar una matriz y 5 para terminar: "))
    match opcion_funcion :
        case 1 :
            numeros = []
            opcion_operacion = int(input("Ingrese 1 para ordenar numeros de mayor a menor, 2 para ordenar numeros de menor a mayor: "))
            def ordenar_numeros(opcion_operacion:int) -> int :
                contador_cambios = 0
                if opcion_operacion == 1 :
                    for i in range(len(numeros)) :
                        for j in range(i + 1, len(numeros)) :
                            if numeros[i] < numeros[j] :
                                aux = numeros[i]
                                numeros[i] = numeros[j]
                                numeros[j] = aux
                                contador_cambios += 1
                elif opcion_operacion == 2:
                    for i in range(len(numeros)) :
                        for j in range(i + 1, len(numeros)) :
                            if numeros[i] > numeros[j] :
                                aux = numeros[i]
                                numeros[i] = numeros[j]
                                numeros[j] = aux
                                contador_cambios += 1
                return contador_cambios
            while True:
                numero = int(input("Ingrese un numero o ingrese 0 para terminar: "))
                if numero == 0 :
                    break
                numeros.append(numero)
            
            resultado = ordenar_numeros(opcion_funcion)
            print(f"Los cambios en total fueron {resultado}")
        
        case 2 :
            nombres = []
            opcion_operacion = int(input("Ingrese 1 para ordenar nombres de la A a la Z o 2 para ordenar nombres de la Z a la A: "))
            def ordenar_nombres(opcion_operacion:int) -> int :
                contador_cambios = 0
                if opcion_operacion == 1:
                    for i in range(len(nombres)) :
                        for j in range(i + 1, len(nombres)) :
                            if nombres[i] > nombres[j] :
                                aux = nombres[i]
                                nombres[i] = nombres[j]
                                nombres[j] = aux
                                contador_cambios += 1
                elif opcion_operacion == 2 :
                    for i in range(len(nombres)) :
                        for j in range(i + 1, len(nombres)) :
                            if nombres[i] < nombres[j] :
                                aux = nombres[i]
                                nombres[i] = nombres[j]
                                nombres[j] = aux
                                contador_cambios += 1
                return contador_cambios
            while True:
                nombre = input("Ingrese un nombre o ingrese terminar para finalizar: ")
                nombre.lower()
                if nombre == "terminar" :
                    break
                nombres.append(nombre)
            
            resultado = ordenar_nombres(opcion_operacion)
            print(nombres)
            print(f"Los cambios en total fueron {resultado}")
        
        case 3 :
            nombres = []
            opcion_operacion = int(input("Ingrese 1 para ordenar nombres, por su largo, de la A a la Z o 2 para ordenar nombres, por su largo, de la Z a la A: "))
            def ordenar_nombres_largo(opcion_operacion:int) -> int :
                contador_cambios = 0
                if opcion_operacion == 1:
                    for i in range(len(nombres)) :
                        for j in range(i + 1, len(nombres)) :
                            if len(nombres[i]) < len(nombres[j]) :
                                aux = nombres[i]
                                nombres[i] = nombres[j]
                                nombres[j] = aux
                                contador_cambios += 1
                elif opcion_operacion == 2 :
                    for i in range(len(nombres)) :
                        for j in range(i + 1, len(nombres)) :
                            if len(nombres[i]) > len(nombres[j]) :
                                aux = nombres[i]
                                nombres[i] = nombres[j]
                                nombres[j] = aux
                                contador_cambios += 1
                return contador_cambios
            while True:
                nombre = input("Ingrese un nombre o ingrese terminar para finalizar: ")
                nombre.lower()
                if nombre == "terminar" :
                    break
                nombres.append(nombre)
            
            resultado = ordenar_nombres_largo(opcion_operacion)
            print(nombres)
            print(f"Los cambios en total fueron {resultado}")
        
        case 4 :
            matriz_nombres_apellidos = []
            datos_cliente_1 = []
            opcion_operacion = int(input("Ingrese 1 para ordenar nombres, por su largo, de la A a la Z o 2 para ordenar nombres, por su largo, de la Z a la A: "))
            prioridad = input("Ingrese 1 para que se ordene por nombre y apellido o 2 para que se ordene de apellido y nombre: ")
            def ordenar_matriz(opcion_operacion:int, prioridad:int) :
                if opcion_operacion == 1 and prioridad == 1 :
                    for i in range(len(matriz_nombres_apellidos)) :
                        for j in range(i + 1, len(matriz_nombres_apellidos)) :
                            if matriz_nombres_apellidos[i][prioridad] > matriz_nombres_apellidos[j][prioridad] :
                                aux = matriz_nombres_apellidos[i]
                                matriz_nombres_apellidos[i] = matriz_nombres_apellidos[j]
                                matriz_nombres_apellidos[j] = aux
                else :
                    for i in range(len(matriz_nombres_apellidos)) :
                        for j in range(i + 1, len(matriz_nombres_apellidos)) :
                            if matriz_nombres_apellidos[i][prioridad] < matriz_nombres_apellidos[j][prioridad] :
                                aux = matriz_nombres_apellidos[i]
                                matriz_nombres_apellidos[i] = matriz_nombres_apellidos[j]
                                matriz_nombres_apellidos[j] = aux

            while True:
                    nombre_apellido = input("Ingrese su nombre y luego su apellido y por ultimo ingrese terminar para finalizar: ")
                    nombre_apellido.lower()
                    if nombre_apellido == "terminar" :
                        break
                    datos_cliente_1.append(nombre_apellido)
                    matriz_nombres_apellidos.append(datos_cliente_1)


            ordenar_matriz(opcion_operacion, prioridad)
            print(matriz_nombres_apellidos)

        case 5 :
            print("Que tenga buen dia :)")
            break


