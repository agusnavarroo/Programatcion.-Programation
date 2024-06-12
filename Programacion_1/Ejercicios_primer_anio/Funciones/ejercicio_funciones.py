'''
Ejercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir
el radio como parámetro y devolver el área.

'''

# import funciones (importa todo lo que esta en el archivo funciones y para usarlo hay que colocar funciones.nombre de la funcion a utilizar)
# from funciones import * (igual que el import funciones pero no hace falta poner el funciones.)
# from funciones import y el nombre de la funcion a utilizar)
# import funciones as F (esto sirve para renombrar o ponerle un apodo a las funciones que importamos desde el archivo funciones, o el archivo que sea. Para no ponerle funciones. y poner F.)
while True :
    opcion = input("Seleccione que funcion desea ejecutar, siendo 1 calcular el area de un circulo, 2 verificar si un numero es par o impar, 3 obteniendo el numero de mayor valor y 4 resultado de la potencia de un numero y su exponente. O escriba terminar para finalizar el programa: ")
    if str(opcion) == "terminar" :
        break
    if int(opcion) == 1 :
        def calcular_area_circulo(radio:float,pi = 3.14) :
            area = pi * (radio ** 2)
            return area

        radio = float(input("Introduzca el area del circulo: "))
        area_circulo = calcular_area_circulo(radio)
        print(f"El area del circulo es: {area_circulo}") # No pide print

    if int(opcion) == 2 :
        def mostrar_par_impar(numero:int) :
            if numero % 2 == 0 :
                print("El numero es par")

            else :
                print("El numero es impar")

        numero = int(input("Ingrese un numero: "))
        mostrar_par_impar(numero)

    if int(opcion) == 3 :
        def encontrar_maximo_de_tres_numeros(numero_uno:int,numero_dos:int,numero_tres:int) :
            if numero_uno > numero_dos and numero_uno > numero_tres :
                numero_mas_grande = numero_uno

            elif numero_dos > numero_uno and numero_dos > numero_tres :
                numero_mas_grande = numero_dos

            else :
                numero_mas_grande = numero_tres

            return numero_mas_grande
        numero_uno = int(input("Ingrese el primer numero: "))
        numero_dos = int(input("Ingrese el segundo numero: "))
        numero_tres = int(input("Ingrese el tercer numero: "))
        numero_maximo = encontrar_maximo_de_tres_numeros(numero_uno,numero_dos,numero_tres)
        print(f"El numero mas grande es: {numero_maximo}")

    if int(opcion) == 4 :
        def calcular_potencia(numero_base:int,numero_exponente:int) :
            resultado = numero_base ** numero_exponente
            return resultado

        numero_base = int(input("Introduzca el numero base: "))
        numero_exponente = int(input("Introduzca el numero exponente: "))
        resultado_final = calcular_potencia(numero_base,numero_exponente)
        print(f"El resultado es: {resultado_final}")

print("Fin del programa")