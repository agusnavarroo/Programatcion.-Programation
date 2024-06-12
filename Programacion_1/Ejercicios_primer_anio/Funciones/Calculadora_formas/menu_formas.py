from funciones import *
def mostrar_menu() :
    resultado_hipotenusa = 0
    resultado_seno = 0
    resultado_coseno = 0
    resultado_tangente = 0
    resultado_area_triangulo = 0
    resultado_perimetro_triangulo = 0
    resultado_diagonal_rectangulo = 0
    resultado_area_rectangulo = 0
    resultado_perimetro_rectangulo = 0
    resultado_relacion_aspecto = 0
    resultado_diagonal_cuadrado = 0
    resultado_area_cuadrado = 0
    resultado_perimetro_cuadrado = 0
    bandera_numero_uno = 0
    bandera_numero_dos = 0
    bandera_numeros = 1
    while(True):

        opcion = int(input("Ingrese una opcion, siendo 1 para ingresar el primer numero.\n 2 para ingresar el segundo numero.\n 3 para calcular los datos del; triangulo.\n 4 para calcular los resultados del rectangulo.\n 5 para calcular los datos del cuadrado.\n 7 para mostrar todos los resultados.\n 8 para salir.\n Ingrese "))

        match opcion:
            case 1:
                numero_uno = int(input("Ingrese el primer numero: "))
                bandera_numero_uno = 1
            case 2:
                numero_dos = int(input("Ingrese el segundo numero: "))
                bandera_numero_dos = 1
            case 3:
                if bandera_numero_uno == 0 or bandera_numero_dos == 0 :
                    print("Error, debe ingresar los 2 numeros para poder hacer los calculos")
                else :
                    resultado_hipotenusa = calcular_hipotenusa(numero_dos,numero_uno)
                    resultado_seno = calcular_seno(numero_uno,numero_dos)
                    resultado_coseno = calcular_coseno(numero_uno,numero_dos)
                    resultado_tangente=calcular_tangente(numero_uno,numero_dos)
                    resultado_area_triangulo = calcular_area_triangulo(numero_uno,numero_dos)
                    resultado_perimetro_triangulo = calcular_perimetro_triangulo(numero_uno,numero_dos,resultado_hipotenusa)
            case 4:
                    if bandera_numero_uno == 0 or bandera_numero_dos == 0 :
                        print("Error, debe ingresar los 2 numeros para poder hacer los calculos")
                    else :
                        resultado_diagonal_rectangulo = calcular_diagonal(numero_uno,numero_dos)
                        resultado_area_rectangulo = calcular_area_rectangulo(numero_uno,numero_dos)
                        resultado_perimetro_rectangulo = calcular_perimetro_rectangulo(numero_uno,numero_dos)
                        resultado_relacion_aspecto = calcular_relacion_de_aspecto(numero_uno,numero_dos)
            case 5:
                    if bandera_numero_uno == 0 or bandera_numero_dos == 0 :
                        print("Error, debe ingresar los 2 numeros para poder hacer los calculos")
                    else :
                        resultado_diagonal_cuadrado = calcular_diagonal_cuadrado(numero_uno,numero_dos)
                        resultado_area_cuadrado = calcular_area_cuadrado(numero_uno,numero_dos)
                        resultado_perimetro_cuadrado = calcular_perimetro_cuadrado(numero_uno,numero_dos)
            case 6:
                if bandera_numeros == 1 :
                    print("Error, no ingreso correctamente los numeros")
                else: 
                    print(f"La hipotenusa vale: {resultado_hipotenusa}")
                    print(f"El seno vale: {resultado_seno}")
                    print(f"El coseno vale: {resultado_coseno}")
                    print(f"La tangente vale: {resultado_tangente}")
                    print(f"El area del triangulo vale: {resultado_area_triangulo}")
                    print(f"El perimetro del triangulo vale: {resultado_perimetro_triangulo}")
                    print(f"La diagonal del rectangulo vale: {resultado_diagonal_rectangulo}")
                    print(f"El area del triangulo vale: {resultado_area_rectangulo}")
                    print(f"El perimetro del triangulo vale: {resultado_perimetro_rectangulo}")
                    print(f"La relacion de aspecto del rectangulo vale: {resultado_relacion_aspecto}")
                    print(f"La diagonal del cuadrado vale: {resultado_diagonal_cuadrado}")
                    print(f"El area del cuadrado vale: {resultado_area_cuadrado}")
                    print(f"El perimetro del cuadrado vale: {resultado_perimetro_cuadrado}")
            case 7:
                print("Datos guardados borrados")
                numero_uno.clear()
                numero_dos.clear()
            case 8:
                print("Fin del programa")
                bandera_numero_uno = 0
                bandera_numero_dos = 0
                break
mostrar_menu()