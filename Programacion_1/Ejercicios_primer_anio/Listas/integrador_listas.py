'''
En un local de venta de zapatillas, se necesita desarrollar un programa para llevar un
registro de las compras realizadas durante toda una semana. El programa debe permitir al
usuario ingresar las compras diarias y calcular ciertas estadísticas al final de la semana.

Funcionalidades del Programa:
1. Registro de Ingresos: El usuario podrá guardar en una única lista los ingresos totales
realizados durante cada día de la semana.
2. Análisis de Datos:
● Determinar el día con más ingresos.
● Determinar el día con menos ingresos.
● Calcular el promedio de ingresos en la semana.
● Calcular el total de ingresos en la semana.
● Calcular el promedio de ingresos en días laborables (de lunes a viernes) y en
días del fin de semana (sábado y domingo).
● Calcular el día con la mayor variación en los ingresos respecto al día anterior.
3. Muestra de datos: Una vez calculados todos los datos del punto 2, se deberán
imprimir en pantalla

'''

lista_ingresos = []
lista_dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
ingresos_lunes = int(input("Ingrese los ingresos totales del dia lunes: "))
lista_ingresos.append(ingresos_lunes)
ingresos_martes = int(input("Ingrese los ingresos totales del dia martes: "))
lista_ingresos.append(ingresos_martes)
ingresos_miercoles = int(input("Ingrese los ingresos totales del dia miercoles: "))
lista_ingresos.append(ingresos_miercoles)
ingresos_jueves = int(input("Ingrese los ingresos totales del dia jueves: "))
lista_ingresos.append(ingresos_jueves)
ingresos_viernes = int(input("Ingrese los ingresos totales del dia viernes: "))
lista_ingresos.append(ingresos_viernes)
ingresos_sabado = int(input("Ingrese los ingresos totales del dia sabado: "))
lista_ingresos.append(ingresos_sabado)
ingresos_domingo = int(input("Ingrese los ingresos totales del dia domingo: "))
lista_ingresos.append(ingresos_domingo)

print(f"Los ingresos totales de cada dia de la semana fueron: || Lunes : {lista_ingresos[0]} pesos || Martes : {lista_ingresos[1]} pesos || Miercoles : {lista_ingresos[2]} pesos || Jueves : {lista_ingresos[3]} pesos || Viernes: {lista_ingresos[4]} pesos || Sabado: {lista_ingresos[5]} pesos || Domingo: {lista_ingresos[6]} pesos || ")

def dia_mas_ingresos() :
    if ingresos_lunes > ingresos_martes and ingresos_lunes > ingresos_miercoles and ingresos_lunes > ingresos_jueves and ingresos_lunes > ingresos_viernes and ingresos_lunes > ingresos_sabado and ingresos_lunes > ingresos_domingo :
        print("El dia con mas ingresos fue el Lunes")
    elif ingresos_martes > ingresos_lunes and ingresos_martes > ingresos_miercoles and ingresos_martes > ingresos_jueves and ingresos_martes > ingresos_viernes and ingresos_martes > ingresos_sabado and ingresos_martes > ingresos_domingo :
        print("El dia con mas ingresos fue el martes")
    elif ingresos_miercoles > ingresos_martes and ingresos_miercoles > ingresos_lunes and ingresos_miercoles > ingresos_jueves and ingresos_miercoles > ingresos_viernes and ingresos_miercoles > ingresos_sabado and ingresos_miercoles > ingresos_domingo :
        print("El dia con mas ingresos fue el miercoles")
    elif ingresos_jueves > ingresos_martes and ingresos_jueves > ingresos_miercoles and ingresos_jueves > ingresos_lunes and ingresos_jueves > ingresos_viernes and ingresos_jueves > ingresos_sabado and ingresos_jueves > ingresos_domingo :
        print("El dia con mas ingresos fue el jueves")
    elif ingresos_viernes > ingresos_martes and ingresos_viernes > ingresos_miercoles and ingresos_viernes > ingresos_jueves and ingresos_viernes > ingresos_lunes and ingresos_viernes > ingresos_sabado and ingresos_viernes > ingresos_domingo :
        print("El dia con mas ingresos fue el viernes")
    elif ingresos_sabado > ingresos_martes and ingresos_sabado > ingresos_miercoles and ingresos_sabado > ingresos_jueves and ingresos_sabado > ingresos_viernes and ingresos_sabado > ingresos_lunes and ingresos_sabado > ingresos_domingo :
        print("El dia con mas ingresos fue el sabado")
    else: 
        print("El dia con mas ingresos fue el domingo")

def dia_menos_ingresos() :
    if ingresos_lunes < ingresos_martes and ingresos_lunes < ingresos_miercoles and ingresos_lunes < ingresos_jueves and ingresos_lunes < ingresos_viernes and ingresos_lunes < ingresos_sabado and ingresos_lunes < ingresos_domingo :
        print("El dia con menos ingresos fue el Lunes")
    elif ingresos_martes < ingresos_lunes and ingresos_martes < ingresos_miercoles and ingresos_martes < ingresos_jueves and ingresos_martes < ingresos_viernes and ingresos_martes < ingresos_sabado and ingresos_martes < ingresos_domingo :
        print("El dia con menos ingresos fue el martes")
    elif ingresos_miercoles < ingresos_martes and ingresos_miercoles < ingresos_lunes and ingresos_miercoles < ingresos_jueves and ingresos_miercoles < ingresos_viernes and ingresos_miercoles < ingresos_sabado and ingresos_miercoles < ingresos_domingo :
        print("El dia con menos ingresos fue el miercoles")
    elif ingresos_jueves < ingresos_martes and ingresos_jueves < ingresos_miercoles and ingresos_jueves < ingresos_lunes and ingresos_jueves < ingresos_viernes and ingresos_jueves < ingresos_sabado and ingresos_jueves < ingresos_domingo :
        print("El dia con menos ingresos fue el jueves")
    elif ingresos_viernes < ingresos_martes and ingresos_viernes < ingresos_miercoles and ingresos_viernes < ingresos_jueves and ingresos_viernes < ingresos_lunes and ingresos_viernes < ingresos_sabado and ingresos_viernes < ingresos_domingo :
        print("El dia con menos ingresos fue el viernes")
    elif ingresos_sabado < ingresos_martes and ingresos_sabado < ingresos_miercoles and ingresos_sabado < ingresos_jueves and ingresos_sabado < ingresos_viernes and ingresos_sabado < ingresos_lunes and ingresos_sabado < ingresos_domingo :
        print("El dia con menos ingresos fue el sabado")
    else: 
        print("El dia con menos ingresos fue el domingo")

def calcular_promedio_ingresos() :
    promedio = (ingresos_lunes + ingresos_martes + ingresos_miercoles + ingresos_jueves + ingresos_viernes + ingresos_sabado + ingresos_domingo) / 7
    return promedio

def calcular_total_ingresos() :
    total_ingresos = ingresos_lunes + ingresos_martes + ingresos_miercoles + ingresos_jueves + ingresos_viernes + ingresos_sabado + ingresos_domingo
    return total_ingresos

def calcular_promedio_ingresos_dias_laborales() :
    promedio_ingreso_dias_laborales = (ingresos_lunes + ingresos_martes + ingresos_miercoles + ingresos_jueves + ingresos_viernes) / 5
    return promedio_ingreso_dias_laborales

def calcular_promedio_ingresos_finde_semana() :
    promedio_ingresos_finde_semana = (ingresos_sabado + ingresos_domingo) / 2
    return calcular_promedio_ingresos_finde_semana

def calcular_dia_mayor_variacion() :
    mayor_diferencia = 0
    dia_mayor_diferencia = lista_dias[0]
    for i in range(1,len(lista_ingresos)) :
        diferencia = lista_ingresos[i] - lista_ingresos[i - 1]
        
        if mayor_diferencia < diferencia :
            mayor_diferencia = diferencia
            dia_mayor_diferencia = lista_dias[i]
    return dia_mayor_diferencia


dia_mas_ingresos()
dia_menos_ingresos()
promedio = calcular_promedio_ingresos()
print(f"El promedio de los ingresos de la semana es de {promedio} pesos")
total_ingresos = calcular_total_ingresos()
print(f"El ingreso total de la semana fue de {total_ingresos} pesos")
promedio_ingreso_dias_laborales = calcular_promedio_ingresos_dias_laborales()
print(f"El promedio de los ingresos en los dias laborales fue de {promedio_ingreso_dias_laborales} pesos")
promedio_ingresos_finde_semana = calcular_promedio_ingresos_dias_laborales()
print(f"El promedio de los ingresos de la semana es de {promedio_ingresos_finde_semana} pesos")
dia_mayor_diferencia = calcular_dia_mayor_variacion()
print(f"El dia con mayor diferencia fue el {dia_mayor_diferencia}")