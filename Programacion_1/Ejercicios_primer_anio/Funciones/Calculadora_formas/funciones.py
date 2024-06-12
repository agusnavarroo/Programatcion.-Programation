'''

Deberán realizar una calculadora de formas.
Para ello el programa iniciará y contará con opciones:

1. Ingresar 1er lado (A=x)

2. Ingresar 2do lado(B=y)

3. Calcular datos de un triángulo rectángulo (No se puede acceder si no se
ingresaron los lados)
● Hipotenusa
● Ángulos
● Área
● Perímetro
'''

def calcular_hipotenusa(numero_uno,numero_dos) :
    hipotenusa = (numero_uno ** 2) + (numero_dos ** 2)
    resultado = hipotenusa ** 0.5
    return resultado

def calcular_seno(hipotenusa,numero_dos) :
    seno = numero_dos / hipotenusa
    return seno


def calcular_coseno(hipotenusa,numero_uno) :
    coseno = numero_uno / hipotenusa
    return coseno

def calcular_tangente(numero_dos,numero_uno) :
    tangente = numero_dos / numero_uno
    return tangente

def calcular_area_triangulo(numero_dos,numero_uno) :
    area = (numero_dos * numero_uno) / 2
    return area

def calcular_perimetro_triangulo(hipotenusa,numero_uno,numero_dos) :
    perimetro = hipotenusa + numero_uno + numero_dos
    return perimetro

'''

4. Calcular datos de un rectángulo (No se puede acceder si no se
ingresaron los lados)
● Diagonal
● Área
● Perímetro
● Relación de aspecto

'''
def calcular_diagonal(numero_uno,numero_dos) :
    diagonal = ((numero_uno ** 2) + (numero_dos ** 2)) ** 0.5
    return diagonal

def calcular_area_rectangulo(numero_uno,numero_dos) :
    area = numero_uno * numero_dos
    return area

def calcular_perimetro_rectangulo(numero_uno,numero_dos) :
    perimetro = (numero_uno * 2) + (numero_dos * 2)
    return perimetro

def calcular_relacion_de_aspecto(numero_uno,numero_dos) :
    relacion_aspecto = numero_uno / numero_dos
    return relacion_aspecto

'''

5. Calcular datos de un cuadrado (No se puede acceder si no se ingresaron los
lados)
● Diagonal
● Área
● Perímetro

'''
def calcular_diagonal_cuadrado(numero_uno,numero_dos) :
    diagonal = (2 ** 0,5) * numero_uno
    return diagonal

def calcular_area_cuadrado(numero_uno,numero_dos) :
    area = numero_uno * numero_dos
    return area

def calcular_perimetro_cuadrado(numero_uno,numero_dos) :
    perimetro = numero_uno * 4
    return perimetro

'''

6. Imprimir los datos guardados
7. Borrar datos guardados
8. Salir

'''

