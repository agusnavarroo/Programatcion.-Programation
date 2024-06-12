import datetime
from funciones_examen import *
from os import *

lista_diccionarios_proyectos = parsear_csv("Proyectos.csv")
id_autoincremental = 11

def incrementar_id():
    global id_autoincremental
    id_autoincremental +=1
    
def decrementar_id():
    global id_autoincremental
    id_autoincremental +=-1

def mostrar_menu() :
    while True :
        print("\nBienvenido.\nA continuacion ingrese la opcion que desee.\n1 para ingresar un nuevo proyecto.\n2 para modificar cualquier aspecto del proyecto.\n3 para cancelar cualquier proyecto.\n4 para cambiar el estado de todos los proyectos cuya fecha de finalización ya haya sucedido.\n5 para mostrar todos los proyectos que se encuentren dados de alta e ingresados.\n6 para calcular el promedio de los presupuestos de todos los proyectos.\n7 para buscar un proyecto.\n8 para ordenar los proyectos por cualquiera de sus aspectos.\n9 para volver a dar de alta un proyecto cancelado.\n10 para ingresar un presupuesto y mostar todos los proyectos que superen el presupuesto ingresado.\n11 para ingresar el nombre de un proyecto y mostrar todos aquellos que superen el presupuesto del proyecto ingresado.\n12 para finalizar el programa.\n13 para\n14 para ")

        opcion = ingresar_opcion("Ingrese la opcion que desee: ", "Error, ingrese una de las opciones disponibles: ", 1, 14)
        system('cls')
        match opcion :
            case 1 :
                incrementar_id()
                if registrar_proyecto(lista_diccionarios_proyectos,id_autoincremental) :
                    print("Proyecto dado de alta correctamente")
                else:
                    decrementar_id()
                    print("No se dio de alta el proyecto")
            case 2 :
                pass
            case 3 :
                pass
            case 4 :
                pass
            case 5 :
                pass
            case 6 :
                pass
            case 7 :
                pass
            case 8 :
                pass
            case 9 : 
                pass
            case 10 :
                pass
            case 11 :
                pass
            case 12 :
                print("Fin del programa")
                break
            case 13 :
                pass
            case 14 :
                pass

mostrar_menu()