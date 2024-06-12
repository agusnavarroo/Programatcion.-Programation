cadena = " Hola Mundo "
cadena_dos = cadena.strip()  #! Strip (Elimina los caracteres vacios del principio y final de un string(aunque se puede elegir si elimina los del principio o final))

print(cadena)
print(cadena_dos)

#* Lower (Convierte , en su totalidad, el texto de una variable a minuscula)

cadena = "Hola Mundo"

print(cadena.lower())

#? Upper (Todo lo contrario a Lower)

cadena = "Agustin"

print(cadena.upper())

# Capitalize (Muestra la primer letra del string en mayuscula y el resto en minuscula, independientemente de como se escriba inicialmente)

cadena = "agusTIn"

print(cadena.capitalize())

#^ Replace (remmplaza ciertas palabras o letras de un string, por otra cosa)

cadena = "La bombonera es el estadio mas hermoso del mundo"

print(cadena.replace("La", ""))

#~ Split (divide elementos de una cadena en subcadenas, debe tener separadores)

cadena = "Agustin Luana Coco Cloyd"
lista_nombres = cadena.split()

print(lista_nombres)

#? Join (contrario al split, de una lista, divide los elementos en una cadena)

lista_nombress = ["Agustin", "Luana", "Coco", "Cloyd"]
separador = ", "
cadena = separador.join(lista_nombress)

print(cadena)

# & Zfill (rellena la cadena con 0 a la izquierda hasta llegar a la cantidad pasada como parametro)

cadena_fill = "56"
print(cadena_fill.zfill(6))

print(cadena_fill.zfill(len(cadena_fill) + 1 )) #! Con esto se puede definir cuantos 0 a la izquierda se desea

# isalpha (Devuelve True si todos los elementos y de una cadena son alfabeticos) (si hay algun tipo de separacion, devuelve False) #! Se usa para validar NOMBRES

cadena = "Esdrujula"

if cadena.isalpha() :
    print("Es alfabetico")
else :
    print("No es alfabetico")

#! isalnum (lo mismo que isalpha, pero si todos los caracteres de la cadena son alfanumericos)

cadena = "666666Jose"

if cadena.isalnum() :
    print("Es alfanumerico")
else :
    print("No es alfanumerico")

# ? Count (cuenta las veces que una letra (subcadena) esta en una cadena)

cadena = "Hola a todos como estan"

print(cadena.count("a"))

# isspace (Verifica que en una cadena unicamente haya espacios)

cadena = " "

if cadena.isspace() :
    print("Tiene unicamente espacios")

else :
    print("No tiene unicamente espacios")