from funciones_reutilizables import *
import os

def parsear_csv(nombre_archivo:str):  # Pasar archivo csv a lista de diccionarios dentro de un 
    '''
    Esta funcion transforma un archivo.csv a una lista de diccionarios
    Recibe como parametro el nombre del archivo, en formato string
    Devuelve la lista de los diccionarios

    '''
    lista_elementos = [] #Lista de alumnos/usuarios/heroes/etc
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r", encoding = 'utf-8') as archivo:
            primer_linea = archivo.readline()
            primer_linea = primer_linea.replace("\n","")
            lista_claves = primer_linea.split(",")
            #print(lista_claves)
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")
                diccionario_aux = {} #Alumno/Usuario/Heroe/Etc
                
                for i in range(len(lista_claves)):
                    diccionario_aux[lista_claves[i]] = lista_valores[i]
                
                #print(diccionario)
                lista_elementos.append(diccionario_aux)
                #print(lista_valores)
        
        return lista_elementos
    else:
        # return False #MANEJAR EL MENSAJE DESDE EL MENU
        print("ARCHIVO NO ENCONTRADO")

lista_diccionarios_proyectos = parsear_csv("Proyectos.csv")

def registrar_proyecto(lista_diccionarios_proyectos:list,id_autoincremental:int) :
    retorno = False
    
    nombre_proyecto = ingresar_str_alfabetico("Ingrese el nombre del proyecto. No debe tener mas de 30 caracteres y debe ser alfabetico: ", "Error, ingrese el nombre del proyecto correctamente: ")
    descripcion_proyecto = ingresar_str_alfanumerico("Ingrese la descripcion del proyecto. No debe tener mas de 200 caracteres y debe ser alfanumerico: ", "Error, ingrese la descripcion del proyecto correctamente: ")
    fechas = comparar_fechas()
    presupuesto = ingresar_entero("Ingrese el presupuesto que dispone el proyecto, no debe ser menor a 500.000: ", "Error, ingrese el presupuesto correctamente: ")
    estado = definir_estado()

    proyecto = {"id":id_autoincremental,"Nombre del Poyecto":nombre_proyecto,"Descripcion":descripcion_proyecto,"Fecha de inicio":fechas,"Fecha de Fin":fechas,"Presupuesto":presupuesto,"Estado": estado}

    # mostrar_proyecto(proyecto) #! DESPUES DE TESTEAR, BORRAR

    if confirmar("\nConfirme con S o N para dar de alta el proyecto: ","\nERROR/Debe elegir entre (S/N) para dar de alta el proyecto: "):
        lista_diccionarios_proyectos.append(proyecto)
        retorno = True
    
    return retorno

# registrar_proyecto()
# print(lista_diccionarios_proyectos)

