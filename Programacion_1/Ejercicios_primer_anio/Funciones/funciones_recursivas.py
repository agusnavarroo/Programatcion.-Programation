'''
1. Realizar una función recursiva que calcule la suma de los primeros números naturales
2. Realizar una función recursiva que calcule la potencia de un número
3. Realizar una función recursiva que la suma de los dígitos de un número
4. Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La
función deberá seguir el siguiente prototipo

'''
# 1) 

def calcular_numeros_naturales(numero:int) -> int :
    if numero <= 1 :
        return numero
    else :
        resultado = numero + calcular_numeros_naturales(numero - 1)
        return resultado


numero = int(input("Ingrese el numero hasta donde quiere que se sumar: "))
valor = calcular_numeros_naturales(numero)
print(f"El resultado es: {valor}")


# 2) 

def calcular_potencia(numero:int,exponente:int) -> int :
    if exponente == 0 :
        resultado = 1
    else :
        resultado = numero * calcular_potencia(numero,exponente - 1)
    return resultado

numero = int(input("Ingrese el numero: "))
exponente = int(input("Ingrese el exponente: "))
valor = calcular_potencia(numero,exponente)
print(f"El resultado es: {valor}")

# 3)

def sumar_digitos(numero:int) -> int :
    if numero == 0 :
        return numero
    else :
        ultimo_digito = numero % 10
        resto_ultimo_digito = numero // 10
        return ultimo_digito + sumar_digitos(resto_ultimo_digito)

numero = int(input("Ingrese el numero hasta donde quiere que se sumar: "))
valor = sumar_digitos(numero)
print(f"El resultado es: {valor}")

# 4)

def calcular_fibonacci(numero:int) -> int :
    if numero == 0 :
        resultado = 0
    elif numero == 1 :
        resultado = 1
    else : 
        resultado = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
    return resultado

numero = int(input("Ingrese el numero: "))
valor = calcular_fibonacci(numero)
print(f"El resultado es: {valor}")
