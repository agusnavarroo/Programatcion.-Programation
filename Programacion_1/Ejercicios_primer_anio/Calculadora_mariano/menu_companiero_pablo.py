from funciones_companiero_pablo import *

def menu():
    resultado_suma = 0
    resultado_resta = 0
    resultado_division = 0
    resultado_multiplicacion = 0
    resultado_potencia = 0
    resultado_resto = 0
    resultado_factorial = 0
    bandera_operando_a = True
    bandera_operando_b = True
    bandera_operaciones = True
    
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = tomar_numero("ingrese opcion")
        
        if opcion == 1:
            operando_a = tomar_numero("ingrese operador a: ")
            bandera_operando_a = False

        elif opcion == 2:
            operando_b = tomar_numero("ingrese operador b: ")
            bandera_operando_b = False

        elif opcion == 3:
            print("Calculo todas las operaciones")
            if bandera_operando_a == True  or bandera_operando_b == True:  
                print("Error INGRESE VALOR DE OPERANDOS")
            else:
                resultado_suma = calcular_suma(operando_a,operando_b)
                resultado_resta = calcular_resta(operando_a,operando_b)
                resultado_division = calcular_division(operando_a,operando_b)
                resultado_multiplicacion = calcular_multiplicacion(operando_a,operando_b)
                resultado_potencia = calcular_potencia(operando_a,operando_b)
                resultado_resto = calcular_resto(operando_a,operando_b)
                resultado_factorial = calcular_factorial(operando_a)
                bandera_operaciones = False

        elif opcion == 4:
            if bandera_operaciones == True:
                print("Error no ingreso correctamente los operandos")

            print("Informo todos los resultados")
            print(f"El resultado de la suma es {resultado_suma}")
            print(f"El resultado de la resta es {resultado_resta}")
            print(f"El resultado de la division es {resultado_division}")
            print(f"El resultado de la multiplicacion es {resultado_multiplicacion}")
            print(f"El resultado de la potencia es {resultado_potencia}")
            print(f"El resto entre operabdo a y operando b es {resultado_resto}")
            print(f"El factorial de a es {resultado_factorial}")

        elif opcion == 5:
            bandera_operando_a = True
            bandera_operando_b = True
            bandera_operaciones = True
            

        elif opcion == 6:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
            
        
    
    
menu()
