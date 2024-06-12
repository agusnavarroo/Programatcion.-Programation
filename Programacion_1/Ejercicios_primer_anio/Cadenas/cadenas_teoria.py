#cadena = "Hola a todos soy \"Mariano\""
#cadena = 'Hola a todos soy \'Mariano\''
#cadena = "Hola a todos\nMe llamo Mariano"
#cadena = "Hola a todos \tMe llamo Mariano"
#cadena = "Hola a todos \aMe llamo Mariano"
# cadena = """Este texto de ejemplo es muy largo, resultando en un código
# significativamente más largo.
# Continúa en una nueva línea,
# se amplía con una tercera y cuarta línea
# y finalmente termina con un punto y aparte."""

#numero = 50

#Concatenar con el + (Si o si el segundo dato tiene que ser string)
# cadena = "La suma es " 
# print(cadena + str(numero))

#Concatenar con la ,
#cadena = "La suma es:"
#print(cadena,str(numero))
#print(cadena,numero)

#f string

#cadena = f"La suma es: {numero}"
#print(f"{cadena} Hola Mundo {numero}")
#print(cadena)

#.format

#cadena = "La suma es: {0}".format(numero)
#print("{0}{1}".format(cadena,numero))
#print(cadena)

#Concatenando con %

numero = 50
numero_dos = 100
PI = 3.14
#cadena = "El numero es %d" %numero
#cadena = "El numero es %f" %PI

#saludo = "20"
#cadena = "Mariano %s Chau" %numero

#cadena = "Hola %x y %x" %(numero,200)
#print(cadena)


#print(f"numero + numero_dos = {numero + numero_dos}")

saludo = "Hola Mundo"

#print(saludo*5)

# if "Lalala" not in saludo:
#     print("True")
# else:
#     print("False")
    
#cadena = "Mariano hola a todos como esta mañana sera lindo dia"
cadena = "Mariano"
#cadena = "Jose"
cadena_aux = ""

# for i in range(len(cadena)):
#     letra = cadena[i]
#     if letra == "a":
#         letra = letra.upper()
#     cadena_aux+=letra

# print(cadena_aux)

#print(cadena[-1])

#Cuento la cantidad de a en mi cadena
contador = 0

# for i in range(len(cadena)):
#     if cadena[i] == "a":
#         contador+=1

# for letra in cadena:
#     if letra == "a" or letra == "A":
#         contador+=1
        
# print(f"El texto tenia {contador} letras a")

#SLICE

#cadena = "Mariano"
#cadena = "Mariano"
#cadena_dos = cadena[0:3] #Primeros 3 caracteres

#cadena_dos = cadena[0::2]

#print(cadena_dos)

cadena = "hola"

print(cadena[4])