from datetime import *

'''
Cosas faltantes o a #? Revisar:

* Como colocar el replace en nombre y descripcion del proyecto
* Como solucionar el tema del estado del proyecto, pido 2 veces las fechas de inicio y fin para definir el estado del proyecto
* Como colocar comilla simple adelante y atras de la cantidad de presupuesto en los proyectos ingresados sin que devuelva none la funcion
#? Revisar la funcion definir estado, devuelve siempre activo
#? Como hago para poner tanto la fecha de fin como la de inicio en el diccionario proyecto sin desarmar la funcion de comparacion
* Opcion del 2 al 11

'''

def ingresar_str_alfabetico(mensaje:str,mensaje_error:str) :
    '''
    Esta funcion valida si el dato ingresado no tiene mas de 30 caracteres, es alfabetico y no contiene caracteres especiales
    Recibe un mensaje para ingresar el dato y un mensaje de error en caso de que el usuario ingrese el dato correctamente
    Devuelve el dato
    '''
    dato = input(mensaje)
    dato.isalpha()
    while len(dato) == 0 or len(dato) > 30 or not dato.isalpha():
        dato = input(mensaje_error)

    return dato.capitalize()

def ingresar_str_alfanumerico(mensaje:str,mensaje_error:str) :
    dato = input(mensaje)
    dato.isalnum()
    while len(dato) == 0 or len(dato) > 200 or not dato.isalnum():
        dato = input(mensaje_error)

    return dato.capitalize()

def ingresar_fechas(mensaje:str) :
    fecha = input(mensaje)
    fecha = datetime.strptime(fecha, "%d-%m-%Y")

    return fecha

def comparar_fechas() :
    fecha_inicio = ingresar_fechas("Ingrese la fecha de inicio del proyecto en formato DD-MM-AAAA: ")
    fecha_fin = ingresar_fechas("Ingrese la fecha de finalizacion del proyecto en formato DD-MM-AAAA: ")
    while fecha_fin < fecha_inicio :
            print("Error, la fecha de finalizacion no puede ocurrir antes de la fecha de inicio del proyecto, reintente.")
            fecha_inicio = ingresar_fechas("Ingrese la fecha de inicio del proyecto en formato DD-MM-AAAA: ")
            fecha_fin = ingresar_fechas("Ingrese la fecha de finalizacion del proyecto en formato DD-MM-AAAA: ")
    
    fecha_inicio = fecha_inicio.strftime("%d-%m-%Y")
    fecha_fin = fecha_fin.strftime("%d-%m-%Y")

    return fecha_inicio.replace("(", "").replace(")", ""), fecha_fin.replace("(", "").replace(")", "")


def ingresar_entero(mensaje:str, mensaje_error:str) :
    dato = int(input(mensaje))

    while dato < 500000 :
        dato = int(input(mensaje_error))
    
    return dato

def definir_estado() :
    # El estado del proyecto sera activo siempre y cuando la fecha de hoy no supere a la de finalizacion o que el proyecto se cancele.
    lista = comparar_fechas() # Esto es para definir el estado del proyecto #! Como obtengo el valor de la fecha de fin sin llamar a la funcion?
    fecha_finalizacion = lista[1]
    fecha_actual = datetime.now().strftime("%d-%m-%Y")
    estado = ""
    if fecha_actual > fecha_finalizacion :
        estado == "Finalizado"

    else :
        estado == "Activo"

    return estado

def ingresar_opcion(mensaje:str,mensaje_error:str,valor_min:int,valor_maximo:int) :
    opcion = int(input(mensaje))

    while opcion < 1 or opcion > valor_maximo :
        opcion = int(input(mensaje_error))

    return opcion

def confirmar(mensaje:str,mensaje_error:str):
    confirmacion = input(mensaje)
    confirmacion = confirmacion.upper()
    retorno = False
    
    while confirmacion != "S" and confirmacion != "N":
        confirmacion = input(mensaje_error)
        confirmacion = confirmacion.upper()
        
    if confirmacion == "S":
        retorno = True

    return retorno

# def mostrar_proyecto(proyecto:dict): #! DESPUES DE TESTEAR, BORRAR
#     informacion = "\nID | NOMBRE | DESCRIPCION | FECHA DE INICIO | FECHA DE FIN | PRESUPUESTO | ESTADO |\n"
#     for clave in proyecto:            
#         if clave != "estado":
#             informacion += str(proyecto[clave]) + " | "
            
#     print(informacion)

while True :
    validacion = comparar_fechas()
    print(validacion)