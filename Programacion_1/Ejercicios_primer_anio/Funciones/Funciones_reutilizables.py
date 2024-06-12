import os
from os import system
from datetime import datetime
import json

def ingresar_bool(mensaje:str, mensaje_error:str) :
    '''
    Esta funcion permite darle un valor de True o False a una variable booleana
    Recibe una variable booleana
    Devuelve la variable booleana

    '''
    estado = "Activo"
    estado.capitalize()
    estado = input(mensaje)
    estado.capitalize()

    if estado == "activo" :
        estado == True
    elif estado == "cancelado" or estado == "finalizado" :
        estado == False

    return estado

def ingresar_string(mensaje:str,mensaje_error:str):
    dato = input(mensaje)
    dato = dato.capitalize()
    
    while (len(dato) == 0) or (len(dato) > 30) or (not dato.isalpha()):
        dato = input(mensaje_error)
        dato = dato.capitalize()
        
    return dato

def ingresar_str_alfabetico(mensaje:str,mensaje_error:str):
    '''
    Esta funcion permite ingresar un dato de tipo entero, validando que sea alfabetico y que no tenga mas de 30 caracteres ni ningun caracter especial
    Recibe un dato string
    Devuelve el mismo dato string

    '''

    dato = input(mensaje)
    dato = dato.capitalize()
    
    while (len(dato) == 0) or (len(dato) > 30) or (not dato.isalpha()):
        dato = input(mensaje_error)
        dato = dato.capitalize()
        
    return dato

def ingresar_str_alfanumerico(mensaje:str,mensaje_error:str):
    '''
    Esta funcion permite ingresar un dato de tipo entero, validando que sea alfanumerico y que no tenga mas de 200 caracteres ni ningun caracter especial
    Recibe un dato string
    Devuelve el mismo dato string

    '''

    dato = input(mensaje)
    dato = dato.capitalize()
    
    while (len(dato) == 0) or (len(dato) > 200) or (not dato.isalnum()):
        dato = input(mensaje_error)
        dato = dato.capitalize()
        
    return dato

def ingresar_genero(mensaje:str,mensaje_error:str):
    genero = input(mensaje)
    genero = genero.upper()
    
    while genero != "F" and genero != "M" and genero != "NB":
        genero = input(mensaje_error)
        genero = genero.upper()
        
    return genero

def ingresar_entero(mensaje:str,mensaje_error:str,valor_min:int):
    numero = int(input(mensaje))
    
    while numero < valor_min:
        numero = int(input(mensaje_error))
        
    return numero
        

def incrementar_id():
    global id_auto_incremental
    id_auto_incremental +=1
    
def decrementar_id():
    global id_auto_incremental
    id_auto_incremental +=-1
    
def imprimir_menu():
    #NO TOCAR
    # system('clear') #Linux/Mac
    system('cls') #Windows
    print("MENU PRINCIPAL\n\n1)Dar de alta un alumno \n2)Modificar Alumno \n3)Dar de Baja a un alumno \n4)Mostrar todos los alumnos\n5)Salir del programa")

def ingresar_fecha_inicio():
    '''
    Esta funcion permite ingresar fechas (dia, mes y anio)
    Devuelve los datos tipo enteros en formato DD/MM/AAAA

    '''
    dia = int(input("Ingrese el dia de inicio del proyecto: "))
    while (dia < 1 or dia > 31):
        dia = int(input("Ingrese correctamente el dia de inicio del proyecto: "))

    mes = int(input("Ingrese el mes de inicio del proyecto: "))
    while (mes < 1 or mes > 12):
        mes = int(input("Ingrese correctamente el mes de inicio del proyecto: "))

    anio = int(input("Ingrese el año de inicio del proyecto: "))
    while (anio < 2010 or anio > 2024):
        anio = int(input("Ingrese correctamente el año de inicio del proyecto: "))

    fecha_inicio = f"{dia}/{mes}/{anio}"
    fecha_inicio = datetime(anio, mes, dia) 

    return fecha_inicio

def ingresar_fecha_fin():
    '''
    Esta funcion permite ingresar fechas (dia, mes y anio)
    Devuelve los datos tipo enteros en formato DD/MM/AAAA

    '''
    dia = int(input("Ingrese el dia de fin del proyecto: "))
    while (dia < 1 or dia > 31):
        dia = int(input("Ingrese correctamente el dia de fin del proyecto: "))

    mes = int(input("Ingrese el mes de fin del proyecto: "))
    while (mes < 1 or mes > 12):
        mes = int(input("Ingrese correctamente el mes de fin del proyecto: "))

    anio = int(input("Ingrese el año de fin del proyecto: "))
    while (anio < 2010 or anio > 2024):
        anio = int(input("Ingrese correctamente el año de fin del proyecto: "))

    fecha_fin = f"{dia}/{mes}/{anio}"
    fecha_fin = datetime(anio, mes, dia)
    return fecha_fin


#PARSER -> Conversion 
#Pasar del archivo CSV a una lista de diccionarios

#! En el parcial lo primero que va es la funcion parse (trae el archivo al programa) y cuando se sale del programa se coloca el generar csv (saca la lista al archivo)

def parse_csv(nombre_archivo:str):  # Pasar archivo csv a lista de diccionarios dentro de un programa
    lista_elementos = [] #Lista de alumnos/usuarios/heroes/etc
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r") as archivo:
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

def generar_csv(nombre_archivo:str,lista:list): #! Pasar de lista de diccionarios a archivo csv
    if len(lista) > 0:
        lista_claves = list(lista[0].keys())
        separador = ","
        cabecera = separador.join(lista_claves)
        print(cabecera)
        
        with open(nombre_archivo,"w") as archivo:
            archivo.write(cabecera + "\n")
            for elemento in lista:
                lista_valores = list(elemento.values())
                for i in range(len(lista_valores)):
                    lista_valores[i] = str(lista_valores[i])

                dato = separador.join(lista_valores)
                dato += "\n"
                archivo.write(dato)
    else:
        print("ERROR LISTA VACIA")
        
def parse_json(nombre_archivo:str): #? Lo mismo que lo anterior pero solo para archivo json
    lista_elementos = []
    
    with open(nombre_archivo,"r") as archivo:
        lista_elementos = json.load(archivo)
    
    return lista_elementos

def generar_json(nombre_archivo:str,lista:list): #^ Lo mismo que la primera pero unicamente para archivo json
    with open(nombre_archivo,"w") as archivo:
        json.dump(lista,archivo,indent=4)
        
lista_usuarios = []

usuario_uno = {"nombre":"Mariano","edad":30}
usuario_dos = {"nombre":"Jose","edad":40}
usuario_tres = {"nombre":"Maria","edad":50}

lista_usuarios.append(usuario_uno)
lista_usuarios.append(usuario_dos)
lista_usuarios.append(usuario_tres)

generar_json("usuarios.json",lista_usuarios)

generar_csv("usuarios.csv",lista_usuarios)
lista_alumnos = parse_json("alumnos.json")

print(lista_alumnos)
        
# lista_alumnos = parse_csv("alumnos.csv")

# print(lista_alumnos[0])

# diccionario = {}

# diccionario["nombre"] = "Mariano"

# print(diccionario)
