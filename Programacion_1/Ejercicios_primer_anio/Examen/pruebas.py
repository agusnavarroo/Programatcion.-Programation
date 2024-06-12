from datetime import datetime
import os

def parsear_csv(nombre_archivo:str):  # Pasar archivo csv a lista de diccionarios dentro de un 
    '''
    Esta funcion transforma un archivo.csv a una lista de diccionarios
    Recibe como parametro el nombre del archivo, en formato string
    Devuelve la lista de los diccionarios

    '''
    lista_elementos = [] #Lista de alumnos/usuarios/heroes/etc
    if os.path.exists(nombre_archivo): # Para que encuentre el archivo, debe estar en una carpeta distinta que la del archivo de este codigo
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
print("| ")
