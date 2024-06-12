import os
import json

#PARSER -> Conversion 
#Pasar del archivo CSV a una lista de diccionarios

#! En el parcial lo primero que va es la funcion parse (trae el archivo al programa) y cuando se sale del programa se coloca el generar csv (saca la lista al archivo)

def parse_csv(nombre_archivo:str):  # Pasar archivo csv a lista de diccionarios dentro de un 
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


# def parse_proyectos(nombre_archivo:str): 
    '''
    Esta funcion transforma un archivo.csv a una lista de diccionarios
    Recibe como parametro el nombre del archivo, en formato string
    Devuelve la lista de los diccionarios

    '''
#     lista_elementos = [] 
#     if os.path.exists(nombre_archivo):
#         with open(nombre_archivo,"r", encoding='utf-8') as archivo:
#             primer_linea = archivo.readline()
#             primer_linea = primer_linea.replace("\n","")
#             lista_claves = primer_linea.split(",")
#             # lista_claves = ["id","Nombre del Proyecto","Descripción","Fecha de inicio","Fecha de Fin","Presupuesto","Estado"]
#             for linea in archivo:
#                 linea_aux = linea.replace("\n", "")
#                 # linea_aux = 1,Plataforma de Gestión Empresarial,Sistema de gestión,13-10-2023,17-04-2025,"$42,931,805.00",Activo
#                 lista_aux = linea_aux.split('"') # Creo una lista auxiliar dividiendo a la linea aux por las comillas que solo se presentan en presupuesto
#                 # lista_aux = ['1,Plataforma de Gestión Empresarial,Sistema de gestión,13-10-2023,17-04-2025,', '$42,931,805.00', ',Activo']
#                 # lista_aux[1] = '$42,931,805.00'
#                 lista_aux[1] = lista_aux[1].replace(",", "") # Elimino las comas pero solo de el indice [1] (el presupuesto)
#                 lista_aux[1] = lista_aux[1].replace("$", "") # Elimino el simbolo $ para poder trabajar sobre los numeros dentro del programa
#                 # lista_aux[1] = '42931805.00'
#                 linea_aux = "".join(lista_aux) # Creo nuevamente la linea aux pero esta vez juntando las 3 partes de la lista aux
#                 # linea_aux = "1,Plataforma de Gestión Empresarial,Sistema de gestión,13-10-2023,17-04-2025,42931805.00,Activo"
#                 lista_valores = linea_aux.split(",") # Creo la lista de valores separando cada elemento por las comas
#                 # lista_valores = ['1', 'Plataforma de Gestión Empresarial', 'Sistema de gestión', '13-10-2023', '17-04-2025', '42931805.00', 'Activo']
#                 diccionario_aux = {}
#                 for i in range(len(lista_claves)):
#                     diccionario_aux[lista_claves[i]] = lista_valores[i]
#                     #diccionario_aux = {"id":"1","Nombre del Proyecto":"Plataforma de Gestión Empresarial","Descripción":"Sistema de gestión","Fecha de inicio":"13-10-2023","Fecha de Fin":"17-04-2025","Presupuesto":"42931805.00","Estado":"Activo"}

#                 lista_elementos.append(diccionario_aux)     
#         return lista_elementos
#     else:
#         return False

# def generar_csv(nombre_archivo:str,lista:list): #! Pasar de lista de diccionarios a archivo csv
#     if len(lista) > 0:
#         lista_claves = list(lista[0].keys())
#         separador = ","
#         cabecera = separador.join(lista_claves)
#         print(cabecera)
        
#         with open(nombre_archivo,"w") as archivo:
#             archivo.write(cabecera + "\n")
#             for elemento in lista:
#                 lista_valores = list(elemento.values())
#                 for i in range(len(lista_valores)):
#                     lista_valores[i] = str(lista_valores[i])

#                 dato = separador.join(lista_valores)
#                 dato += "\n"
#                 archivo.write(dato)
#     else:
#         print("ERROR LISTA VACIA")
        
# def parse_json(nombre_archivo:str): #? Lo mismo que lo anterior pero solo para archivo json
#     lista_elementos = []
    
#     with open(nombre_archivo,"r") as archivo:
#         lista_elementos = json.load(archivo)
    
#     return lista_elementos

# def generar_json(nombre_archivo:str,lista:list): #^ Lo mismo que la primera pero unicamente para archivo json
#     with open(nombre_archivo,"w") as archivo:
#         json.dump(lista,archivo,indent=4)
        
# lista_usuarios = []

# usuario_uno = {"nombre":"Mariano","edad":30}
# usuario_dos = {"nombre":"Jose","edad":40}
# usuario_tres = {"nombre":"Maria","edad":50}

# lista_usuarios.append(usuario_uno)
# lista_usuarios.append(usuario_dos)
# lista_usuarios.append(usuario_tres)

# generar_json("usuarios.json",lista_usuarios)

# generar_csv("usuarios.csv",lista_usuarios)
# lista_alumnos = parse_json("alumnos.json")

# print(lista_alumnos)
        
# lista_alumnos = parse_csv("alumnos.csv")

# print(lista_alumnos[0])

# diccionario = {}

# diccionario["nombre"] = "Mariano"

# print(diccionario)

