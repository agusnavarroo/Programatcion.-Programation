from funciones_abm import *
from os import *

#Un alumno tiene (id, nombre, apellido, genero, nota final)

lista_alumnos = []

id_auto_incremental = 0

def incrementar_id():
    global id_auto_incremental
    id_auto_incremental +=1
    
def decrementar_id():
    global id_auto_incremental
    id_auto_incremental +=-1
    
def imprimir_menu():
    #NO TOCAR
    system('clear') #Linux/Mac
    #system('cls') #Windows
    print("MENU PRINCIPAL\n\n1)Dar de alta un alumno \n2)Modificar Alumno \n3)Dar de Baja a un alumno \n4)Mostrar todos los alumnos\n5)Salir del programa")


def menu():
    while(True):
        imprimir_menu()
        opcion = int(input("Elija una opción: "))
        #system('clear') #Linux/Mac
        system('cls') #Windows
        match opcion:
            case 1:
                incrementar_id()
                if agregar_alumno(id_auto_incremental,lista_alumnos):
                    print("SE DIO DE ALTA CORRECTAMENTE")
                else:
                    decrementar_id()
                    print("ALTA CANCELADA")
            case 2:
                print("Modificar un Alumno")
            case 3:
                if contar_alumnos_activos(lista_alumnos) > 0:
                    eliminar_alumno(lista_alumnos)
                else:
                    print("NO HAY ALUMNOS DADOS DE ALTA")
            case 4:
                if contar_alumnos_activos(lista_alumnos) > 0:
                    mostrar_alumnos(lista_alumnos)
                else:
                    print("NO HAY ALUMNOS DADOS DE ALTA")
            case 5:
                print("Saliendo del sistema...")
                break
        input("Presione enter para continuar...")
menu()