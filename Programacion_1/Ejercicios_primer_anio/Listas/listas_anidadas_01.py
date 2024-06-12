'''
El programa debe permitir al usuario ingresar los siguientes datos para 10 alumnos:
● Nombre
● Edad
● DNI
● Género (M para masculino, F para femenino, NB para No Binario)
● Nota
Después de ingresar los datos de todos los alumnos, el programa debe calcular y
mostrar la siguiente información:
1. Listado de todos los alumnos con un formato similar al siguiente: 
2. El promedio de edades de los alumnos.  = 30
3. La cantidad de alumnos que promocionaron (nota mayor o igual a 6). = 4
4. La cantidad de alumnos que aprobaron (nota mayor o igual a 4). = 3
5. La cantidad de alumnos que desaprobaron (nota menor a 4). = 3
6. El promedio de nota de los alumnos masculinos. = 4.4
7. El porcentaje de alumnas que promocionaron sobre el total de alumnas. = 15 %

'''

lista_alumnos = []
suma_edades = 0
contador_alumnos_que_promocionaron = 0
contador_alumnos_que_aprobaron = 0
contador_alumnos_que_desaprobaron = 0
sumador_nota = 0
contador_alumnos_masculinos = 0
contador_alumnas_promocionaron = 0
contador_alumnas = 0
for i in range (10) :
    lista_datos = []
    nombre = input("Ingrese su nombre: ")
    lista_datos.append(nombre)
    edad = int(input("Ingrese su edad, debe ser entre 18 y 98: "))
    while edad < 18 or edad >= 99 :
        print("Error, ingrese una edad valida, debe ser entre 18 y 98: ")
        edad = int(input("Ingrese su edad: "))
    lista_datos.append(edad)
    suma_edades += edad
    # dni = int(input("Ingrese su dni, sin espacios, sin punto y sin guion (xxxxxxxx): "))
    # while dni <= 11111111 or dni >= 999999999 :
    #     print("Error, coloque un DNI valido, debe tener 8 numeros")
    #     dni = int(input("Ingrese su dni, sin espacios, sin punto y sin guion (xxxxxxxx): "))
    # lista_datos.append(dni)
    genero = input("Ingrese su genero, debe ser M, F o NB: ")
    while genero != "F" and genero != "M" and genero != "NB" :
        print("Error, ingrese su genero correctamente, debe ser f, m o nb")
        genero = input("Ingrese su genero, debe ser M, F o NB: ")
    if genero == "M" :
        contador_alumnos_masculinos += 1
    elif genero == "F" :
        contador_alumnas += 1
    lista_datos.append(genero)
    nota = int(input("Ingrese su nota, debe ser entre 1 y 10: "))
    while nota < 1 or nota > 10 :
        print("Error, ingrese su nota correctamente. debe ser entre 1 y 10")
        nota = int(input("Ingrese su nota, debe ser entre 1 y 10: "))
    if nota >= 6 :
        contador_alumnos_que_promocionaron += 1
        if genero == "F" :
            contador_alumnas_promocionaron += 1
    if nota >= 4 :
        contador_alumnos_que_aprobaron += 1
    if nota < 4 :
        contador_alumnos_que_desaprobaron += 1
    if genero == "M" :
        sumador_nota += nota
    lista_datos.append(nota)
    lista_alumnos.append(lista_datos)

promedio_edades = suma_edades / 10
alumnos_promocionados = contador_alumnos_que_promocionaron
alumnos_aprobados = contador_alumnos_que_aprobaron
alumnos_desaprobados = contador_alumnos_que_desaprobaron
promedio_notas_masculinos = sumador_nota / contador_alumnos_masculinos
porcentaje_alumnas_que_promocionaron = (contador_alumnas_promocionaron / 100) * contador_alumnas

for lista in lista_alumnos: # Esto se puede realizar solamente si sabemos la cantidad de elementos que tendra la lista
    print(f"||{lista[0]}||{lista[1]}||{lista[2]}||{lista[3]}||")


#for i in range(len(lista_alumnos)): # Esto se puede realizar si no sabemos la cantida de elementos que tendra la lista
#    for j in range(len(lista_alumnos[i])):
#       print( lista_alumnos[i][j])

print(f"El promedio de edad de los alumnos ingresados es de: {promedio_edades}\n Promocionaron {alumnos_promocionados} alumnos\n Aprobaron {alumnos_aprobados} alumnos\n Desaprobaron {alumnos_desaprobados} alumnos\n El promedio de notas de los alumnos masculinos es de {promedio_notas_masculinos}\n El porcentaje de alumnas que promocionaron sobre el total es del {porcentaje_alumnas_que_promocionaron} % ")
