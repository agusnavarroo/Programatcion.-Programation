from funciones import *
# https://onlinegdb.com/8xTXEy4Uid (menu del companiero pablo)
# https://onlinegdb.com/Ls9ghHh20 (funciones del companiero pablo)
# https://onlinegdb.com/JAyYaGIVy (lo de belen mas lo de pablo)


def mostrar_menu():
    resultado_suma = 0
    resultado_resta = 0
    resultado_division = 0
    resultado_multiplicacion = 0
    resultado_potencia = 0
    resultado_potencia = 0
    resultado_factorial = 0
    bandera_numero_uno = False
    bandera_numero_dos = False
    bandera_numeros = True
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = tomar_numeros("Ingrese la opcion: ")
        
        if opcion == 1:
            numero_uno = tomar_numeros("Ingrese el primer numero: ")
            bandera_numero_uno = True
        elif opcion == 2:
            numero_dos = tomar_numeros("Ingrese el segundo numero: ")
            bandera_numero_dos = True
        elif opcion == 3:
            if bandera_numero_uno == False or bandera_numero_dos == False :
                print("Error, debe ingresar si o si un valor para ambos numeros")
            else:
                resultado_suma = calcular_suma(numero_uno,numero_dos)
                resultado_resta = calcular_resta(numero_uno,numero_dos)
                resultado_division = calcular_division(numero_uno,numero_dos)
                resultado_multiplicacion= calcular_multiplicacion(numero_uno,numero_dos)
                resultado_potencia = calcular_potencia(numero_uno,numero_dos)
                resultado_resto = calcular_resto(numero_uno,numero_dos)
                resultado_factorial = calcular_factorial(numero_uno)
                bandera_numeros = False
        elif opcion == 4:
            if bandera_numeros == True :
                print("Error, no ingreso correctamente los numeros")
            print(f"El resultado es: {resultado_suma}")
            print(f"El resultado es: {resultado_resta}")
            print(f"El resultado es: {resultado_division}")
            print(f"El resultado es: {resultado_multiplicacion}")
            print(f"El resultado es: {resultado_potencia}")
            print(f"El resultado es: {resultado_resto}")
            print(f"El resultado es: {resultado_factorial}")
        elif opcion == 5 :
            bandera_numero_uno = False
            bandera_numero_dos = False
            bandera_numeros = True
        elif opcion == 6 :
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-6")
                
mostrar_menu()
