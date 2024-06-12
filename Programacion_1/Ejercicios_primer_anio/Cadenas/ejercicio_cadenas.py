def calcular_cant_vocales(cadena:str) : 
    cant_a = 0
    cant_e = 0
    cant_i = 0
    cant_o = 0
    cant_u = 0
    for i in range(len(cadena)) :
        if cadena[i] == "a" :
            cant_a +=1 
        if cadena[i] == "e":
            cant_e += 1
        if cadena[i] == "i":
            cant_i += 1
        if cadena[i] == "o":
            cant_o += 1
        if cadena[i] == "u":
            cant_u += 1
        matriz = [
            ["a", cant_a]
            ["e", cant_e]
            ["i", cant_i]
            ["o", cant_o]
            ["u", cant_u]
]

    return matriz


cadena = input("Ingrese una palabra: ")
cadena.lower()

resultado = calcular_cant_vocales(cadena)
print(resultado)

