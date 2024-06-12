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
2. El promedio de edades de los alumnos.
3. La cantidad de alumnos que promocionaron (nota mayor o igual a 6).
4. La cantidad de alumnos que aprobaron (nota mayor o igual a 4).
5. La cantidad de alumnos que desaprobaron (nota menor a 4).
6. El promedio de nota de los alumnos masculinos.
7. El porcentaje de alumnas que promocionaron sobre el total de alumnas.

'''

lista_alumnos = []

for i in range(2):
    
    print("")
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    while edad < 18 or edad > 99:
        edad = int(input("Ringrese edad: "))
    dni = int(input("Ingrese su dni: "))
    while dni <= 9999999:
        dni = int(input("Reingrese su dni: "))
    genero = input("Ingrese genero: ")
    while genero != "M" and genero != "F" and genero != "NB":
        genero = input("Reingrese genero: ")
    nota = int(input("Ingrese nota: "))
    while nota < 1 or nota >10:
        nota = int(input("Riengrese nota: "))
    lista_datos = [nombre,edad,dni,genero,nota]
    lista_alumnos.append(lista_datos)

print(lista_alumnos)

#for lista in lista_alumnos:
#  print(f"||{lista[0]}{lista[1]}||{lista[2]}||{lista[3]}||{lista[4]}||")
#for i in range(len(lista_alumnos)):
#    print(f"║{lista_alumnos[i][0]}║{lista_alumnos[i][1]}║{lista_alumnos[i][2]}║{lista_alumnos[i][3]}║{lista_alumnos[i][4]}║")
#for lista in lista_alumnos:
#    for dato in lista:
#        print(dato)

#for i in range(len(lista_alumnos)):
#    for j in range(len(lista_alumnos[i])):
#       print( lista_alumnos[i][j])

#def calcular_promedio(suma, cantidad):
#    promedio = suma / cantidad
#    return promedio

def calcular_promedio_lista(lista:list,indice)-> float: 
    acumulador_edades = 0
    for i in range (len(lista)): 
        acumulador_edades += lista[i][indice]
    promedio = acumulador_edades / len(lista)
    return promedio

#promedio = calcular_promedio_lista(lista_alumnos,1)

#print(promedio)

def calcular_aprobados(lista):
    alumnos_aprobados = 0
    alumnos_desaprobados = 0
    alumnos_promocionados = 0
    for i in range(len(lista)):
        if lista[i][4] >= 6:
            alumnos_promocionados += 1
        elif lista[i][4] >= 4:
            alumnos_aprobados += 1
        else:
            alumnos_desaprobados += 1
    lista_notas = [alumnos_aprobados,alumnos_desaprobados,alumnos_promocionados]

    return lista_notas

# lista_prueba = [[0,0,0,0,10],[0,0,0,0,5],[0,0,0,0,8],[0,0,0,0,3],[0,0,0,0,4]]
# aprobados = calcular_aprobados(lista_prueba,3)
# print(aprobados)

lista_prueba = [[0,0,0,"M",10],[0,0,0,"M",5],[0,0,0,0,8],[0,0,0,0,3],[0,0,0,0,4]]
aprobados = calcular_aprobados(lista_prueba)
print(f"Los aprobados son {aprobados[0]}, los desaprobados son {aprobados[1]} y los promocionados {aprobados[2]}")

def calcular_promedio_masculinos(lista):
    lista_masculinos = []
    for i in range(len(lista)):
        
        if lista[i][3] == "M":
            lista_masculinos.append(lista[i])

    promedio_masculinos = calcular_promedio_lista(lista_masculinos,4)
    return promedio_masculinos
# promedio_masculino = calcular_promedio_masculinos(lista_prueba)
# print(promedio_masculino)