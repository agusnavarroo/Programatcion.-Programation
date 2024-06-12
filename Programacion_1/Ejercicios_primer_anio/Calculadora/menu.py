import os
from funciones import *


def menu():
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            print("Ingreso Primer Operando")
        elif opcion == 2:
            print("Ingreso Segundo Operando")
        elif opcion == 3:
            print("Calculo todas las operaciones")
        elif opcion == 4:
            print("Informo todos los resultados")
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")
            
        os.system('clear')
    
    
menu()
