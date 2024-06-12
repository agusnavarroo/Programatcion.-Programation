'''

Para ello el programa iniciará y contará con un menú de opciones:
1.
2.
3.
4.
Ingresar 1er operando (A=x)
Ingresar 2do operando (B=y)
Calcular todas las operaciones (No se puede acceder si no se ingresaron
los dos operandos)
a) Calcular la suma (A+B)
b) Calcular la resta (A-B)
c) Calcular la división (A/B)
d) Calcular la multiplicación (A*B)
e) Calcular potencia entre (A ** B)
f) Calcular resto entre (A % B)
g) Calcular el factorial (A!)
Informar Resultados (No se puede acceder si no se calcularon las
operaciones)
a) “El resultado de A+B es: r”
b) “El resultado de A-B es: r”
c) “El resultado de A/B es ” o “No es posible dividir por cero”
d) “El resultado de A*B es: r”
e) “A elevado a la B da como resultado r”
f) “El resultado de A % B es ” o “No es posible dividir por cero”
g) “El factorial de A es: r1 y El factorial de B es: r2”
5.
Salir

'''

def tomar_numeros(mensaje) :
    numero_uno = int(input(mensaje))
    return numero_uno

def calcular_suma(numero_uno,numero_dos) :
    suma = numero_uno + numero_dos
    return suma

def calcular_resta(numero_uno,numero_dos) :
    resta = numero_uno - numero_dos
    return resta

def calcular_division(numero_uno,numero_dos) :
    if numero_uno or numero_dos == 0 :
        print("Numero no valido, debe ser mayor a 0")
    else :
        division = numero_uno/numero_dos
        return division

def calcular_multiplicacion(numero_uno,numero_dos) :
    multiplicacion = numero_uno * numero_dos
    return multiplicacion

def calcular_potencia(numero_uno,numero_dos) :
    potencia = numero_uno ** numero_dos
    return potencia

def calcular_resto(numero_uno,numero_dos) :
    resto = numero_uno % numero_dos
    return resto

def calcular_factorial(numero_uno:int) -> int :
    if numero_uno == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero_uno + 1):
            resultado *= i
        return resultado
    


# CALCULAR EL FACTORIAL USANDO FUNCION RECURSIVA
# def calcular_factorial(numero_uno):
#     if numero_uno == 1 or numero_uno == 0 :
#         return 1
#     else :
#         numero_uno * calcular_factorial(numero_uno - 1)


# numero_uno = 5
# print(f"El resultado es: {calcular_factorial(numero_uno)}")
