def calcular_suma(a: int, b: int) -> int:
    """
    Calcula la suma de dos numeros enteros.

    Args:
    a (int): El primer numero entero.
    b (int): El segundo numero entero.

    Returns:
    int: La suma de los dos numeros.
    """
    resultado = a + b
    return resultado


def calcular_resta(a: int, b: int) -> int:
    """
    Calcula la resta de dos numeros enteros.
    a (int): El primer numero entero.
    b (int): El segundo numero entero.
    Returns:
    int: La resta de los dos numeros (a - b).
    """
    resultado = a - b
    return resultado


def calcular_division(a: int, b: int) -> float:
    """
    Calcula la division de dos numeros enteros.
    a (int): El dividendo.
    b (int): El divisor.
    Returns:
    float: El resultado de la division (a / b), si b no es cero.
           None si b es cero.
    """
    if b == 0:

        print("No se puede dividir por cero")
    else:
        resultado = a / b
        return resultado


def calcular_multiplicacion(a: int, b: int) -> int:
    """
    Calcula el producto de dos numeros enteros.
    a (int): El primer numero entero.
    b (int): El segundo numero entero.

    Returns:
    int: El producto de los dos numeros (a * b).
    """
    resultado = a * b
    return resultado

def calcular_potencia(a: int, b: int) -> int:
    """
    Calcula la potencia de un numero entero elevado a otro numero entero.
    a (int): La base.
    b (int): El exponente.
    Returns:
    int: El resultado de la potencia (a^b).
    """
    resultado = a ** b
    return resultado

def calcular_resto(a: int, b: int) -> int:
    """
    Calcula el resto de la division de dos numeros enteros.
    a (int): El dividendo.
    b (int): El divisor.
    Returns:
    int: El resto de la division entera de a entre b (a % b).
    """
    if b == 0:
        
        print("No se puede dividir por cero")
    else:
        resultado = a % b
        return resultado

def calcular_factorial(a:int) -> int :
    """
    Calcula el factorial de un numero entero no negativo 'a' utilizando un bucle for y un rango.
    
    Args:
    - a (int): El numero del cual se calculará el factorial.
    
    Returns:
    - int: El factorial de 'a'.
    """
    if a == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, a + 1):
            resultado *= i
        return resultado


def tomar_numero(mensaje):
        a = input(mensaje)
        a = int(a)
        return a
        