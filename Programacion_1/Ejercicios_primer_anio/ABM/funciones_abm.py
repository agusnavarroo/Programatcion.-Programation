ACTIVO = True
INACTIVO = False

BAJA_CORRECTA = 1
BAJA_ERRONEA = 2
BAJA_CANCELADA = 3

MODIFICACION_CORRECTA = 1
MODIFICACION_ERRONEA = 2
MODIFICACION_CANCELADA = 3

def mostrar_alumnos(lista_alumnos:list):
    informacion = "ALUMNOS\nID | NOMBRE | APELLIDO | GENERO | NOTA FINAL |\n"
    for alumno in lista_alumnos:
        for clave in alumno:
            if alumno["estado"] == ACTIVO:             
                if clave != "estado":
                    informacion += str(alumno[clave]) + " | "
        informacion +="\n"
    print(informacion)


def mostrar_alumno(alumno:dict):
    informacion = "ALUMNOS\nID | NOMBRE | APELLIDO | GENERO | NOTA FINAL |\n"
    for clave in alumno:            
        if clave != "estado":
            informacion += str(alumno[clave]) + " | "
            
    print(informacion)
    
def ingresar_string(mensaje:str,mensaje_error:str):
    dato = input(mensaje)
    dato = dato.capitalize()
    
    while len(dato) == 0:
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

def ingresar_entero(mensaje:str,mensaje_error:str,valor_min:int,valor_max:int):
    numero = int(input(mensaje))
    
    while numero > valor_max or numero < valor_min:
        numero = int(input(mensaje_error))
        
    return numero
        

def agregar_alumno(id_autoincremental:int,lista_alumnos:list):
    retorno = False
    
    nombre_ingresado = ingresar_string("Ingrese su nombre: ","ERROR/Reingrese el nombre (NO PUEDE ESTAR VACIO): ")
    apellido_ingreado = ingresar_string("Ingrese un apellido: ","ERROR/Ingrese un apellido (NO PUEDE ESTAR VACIO): ")
    genero_ingresado = ingresar_genero("Ingrese su genero (M/F/NB): ","ERROR/Ingrese un genero valido (M/F/NB): ")
    nota_final_ingresada = ingresar_entero("Ingrese la nota final (1-10): ","ERROR/Ingrese la nota final (1-10): ",1,10)

    alumno = {"id":id_autoincremental,"nombre":nombre_ingresado,"apellido":apellido_ingreado,"genero":genero_ingresado,"nota_final":nota_final_ingresada,"estado":ACTIVO}
    
    mostrar_alumno(alumno)
    #confirmacion = input("\nConfirma dar de alta el siguiente alumno (S-N)\n")
    
    if confirmar("\nConfirma dar de alta el siguiente alumno (S-N): ","\nERROR/Debe elegir entre (S/N) Confirma dar de alta el siguiente alumno (S-N): "):
        lista_alumnos.append(alumno)
        retorno = True
    
    return retorno

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
    



def buscar_alumno(lista_alumnos:list,id_a_buscar:int):
    retorno = None

    # for alumno in lista_alumnos:
    #     if alumno["id"] == id_a_buscar:
    #         print("Se encontro el alumno")
    #         mostrar_alumno(alumno)
    #         retorno = True 
    #         break
    
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i]["id"] == id_a_buscar and lista_alumnos[i]["estado"] == ACTIVO:
            print("Se encontro el alumno")
            mostrar_alumno(lista_alumnos[i])
            retorno = i
            break
        
    return retorno

def contar_alumnos_activos(lista_alumnos:list):
    contador = 0
    
    for alumno in lista_alumnos:
        if alumno["estado"] == ACTIVO:
            contador+=1
                        
    return contador

def eliminar_alumno(lista_alumnos:list):   
    retorno = BAJA_ERRONEA 
    #Para eliminar el alumno, primero tengo que encontrarlo
    mostrar_alumnos(lista_alumnos)
    
    id_a_eliminar = int(input("Ingrese el id del alumno a eliminar: "))
    indice = buscar_alumno(lista_alumnos,id_a_eliminar)
    
    if indice != None:
        #BAJA FISICA (NO SE HACE)
        #lista_alumnos.pop(indice)
        
        #BAJA LOGICA
        #mostrar_alumno(lista_alumnos[indice])
        if confirmar("\nConfirma dar de baja el siguiente alumno (S-N): ","\nERROR/Debe elegir entre (S/N) Confirma dar de baja el siguiente alumno (S-N): "):
            lista_alumnos[indice]["estado"] = INACTIVO#Alumno
            retorno = BAJA_CORRECTA
        else:
            retorno = BAJA_CANCELADA
    return retorno

def modificar_alumno(lista_alumnos:list):
    retorno = MODIFICACION_ERRONEA 
    mostrar_alumnos(lista_alumnos)
    
    id_a_modificar = int(input("Ingrese el id del alumno a modificar: "))
    indice = buscar_alumno(lista_alumnos,id_a_modificar)
    
    if indice != None:
        #MODIFICARLO
        nombre_ingresado = ingresar_string("Ingrese nombre: ","ERROR/Reingrese el nombre (NO PUEDE ESTAR VACIO): ")
        apellido_ingreado = ingresar_string("Ingrese apellido: ","ERROR/Ingrese un apellido (NO PUEDE ESTAR VACIO): ")
        genero_ingresado = ingresar_genero("Ingrese genero (M/F/NB): ","ERROR/Ingrese un genero valido (M/F/NB): ")
        nota_final_ingresada = ingresar_entero("Ingrese nota final (1-10): ","ERROR/Ingrese la nota final (1-10): ",1,10)

        alumno_aux = {"id":id_a_modificar,"nombre":nombre_ingresado,"apellido":apellido_ingreado,"genero":genero_ingresado,"nota_final":nota_final_ingresada,"estado":ACTIVO}
        
        if confirmar("\nConfirma modificar el siguiente alumno (S-N): ","\nERROR/Debe elegir entre (S/N) Confirma modificar el siguiente alumno (S-N): "):
            lista_alumnos[indice] = alumno_aux
            retorno = MODIFICACION_CORRECTA
        else:
            retorno = MODIFICACION_CANCELADA
    return retorno
