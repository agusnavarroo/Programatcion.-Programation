import datetime

def ingresar_entero(mensaje, mensaje_error, minimo) -> int :
    dato = int(input(mensaje))
    while dato < minimo :
        dato = int(input(mensaje_error))
    
    return dato       # Esta funcion es para pedir los datos ENTEROS de una manera resumida, su mensaje de error y el minimo 

def ingresar_float(mensaje, mensaje_error, minimo) -> float :
    dato = float(input(mensaje))
    while dato < minimo :
        dato = float(input(mensaje_error))
    
    return dato

def ingresar_str(mensaje, mensaje_error) -> str :
    dato = (input(mensaje))
    dato.capitalize()
    while dato == "" :
        dato = (input(mensaje_error))
        dato.capitalize()
    return dato

def ingresar_fecha():
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

    fecha = f"{dia}/{mes}/{anio}"
    return fecha

def registrar_mascota() :
    lista_mascota = []

    
    dni = ingresar_entero("Ingrese el dni: ", "Error, reingrese su dni: ", 1)

    nombre = ingresar_str("Ingrese el nombre de su mascota: ", "Error, nombre no ingresado, reintente: ")

    edad = ingresar_entero("Ingrese la edad de su mascota: ", "Error, edad erronea, reintente", 1)

    especie = ingresar_str("Ingrese la especie de su mascota: ", "Error, especie no ingresada, reintente: ")
    
    sexo = ingresar_str("Ingrese el sexo de su mascota: ", "Error, sexo no ingresada, reintente")

    peso = ingresar_float("Ingrese el peso de su mascota: ", "Error, peso no valido, reintente: ", 1)

    fecha = ingresar_fecha()
    
    historial = ingresar_str("Ingrese el motivo de la consulta: ", "Error, motivo de la consulta no ingresado, reintente: ")

    lista_mascota.append(dni)
    lista_mascota.append(nombre)
    lista_mascota.append(edad)
    lista_mascota.append(especie)
    lista_mascota.append(peso)
    lista_mascota.append(fecha)
    lista_mascota.append(historial)

    return lista_mascota



def buscar_mascota(registro_mascotas:list) :
    mascota_encontrada = None
    nombre = ingresar_str("Ingrese el nombre de la mascota a actualizar: ", "Error, nombre no ingresado, reintente: ")
    for i in range(len(registro_mascotas)) :
        nombre_mascota = registro_mascotas[i][1]
        if nombre_mascota == nombre :
            mascota_encontrada = i
            break
    return mascota_encontrada


def actualizar_mascota(i,registro_mascotas:list) :
    fecha_hoy = datetime.date.today()
    fecha_formato_personalizado = fecha_hoy.strftime("%d/%m/Y")

    nuevo_historial = ingresar_str("Ingrese el motivo de la consulta: ", "Error, motivo de la consulta no ingresado, reintente: ")
    edad_nueva = ingresar_entero("Ingrese la edad de su mascota: ", "Error, edad erronea, reintente", 1)
    peso_nuevo = ingresar_float("Ingrese el peso de su mascota: ", "Error, peso no valido, reintente: ", 1)
    
    # Modifico edad
    registro_mascotas[i][2] = edad_nueva

    # Modifico peso
    registro_mascotas[i][5] = peso_nuevo

    # Modifico fecha
    registro_mascotas[i][6] = fecha_formato_personalizado

    # Modifico historial
    registro_mascotas[i][7] = nuevo_historial

def mostrar_lista_anidada(lista_anidada:list) :
    for i in range(len(lista_anidada)) :
        mensaje = ""
        for j in range(len(lista_anidada[i])) : # Recorro la cantidad de columnas de la lista
            print(f"{lista_anidada[i][j]}", end =" ")
        print("")

def calcular_promedio_edad(registro_mascotas:list) :
    acumulador = 0
    for i in range(len(registro_mascotas)) :
        acumulador = (acumulador + registro_mascotas[i][2])
    promedio = acumulador / len(registro_mascotas)
    print(f"El promedio de edad de las mascotas es de {promedio} anios ")
def calcular_promedio_peso(registro_mascotas:list) :
    acumulador = 0
    for i in range(len(registro_mascotas)) :
        acumulador = (acumulador + registro_mascotas[i][5])
    promedio = acumulador / len(registro_mascotas)
    print(f"El promedio de peos de las mascotas es de {promedio} kilos")

def contar_perros(registro_mascotas:list) :
    contador_perros = 0
    for i in range(len(registro_mascotas)) :
        if registro_mascotas[i][3] == "Perro" or registro_mascotas[i][3] == "perro":
            contador_perros += 1
    print(f"La cantidad de perros son {contador_perros}")

def mostrar_mascota_mas_registrado(registro_mascotas:list) :
    contador_perros = 0
    contador_gatos = 0
    contador_dragones = 0
    for i in range(len(registro_mascotas)) :
        match registro_mascotas[i][3] :
            case "Perro" :
                contador_perros += 1
            case "Gato" :
                contador_gatos += 1 
            case _:
                contador_dragones += 1
    if contador_perros > contador_gatos and contador_perros > contador_dragones :
        print('El tipo de mascota mas registrado fue Perro')
    elif contador_gatos > contador_dragones :
        print('El tipo de mascota mas registrado fue Gato')
    else :
        print("El tipo de mascota mas registrado fue Dragon")