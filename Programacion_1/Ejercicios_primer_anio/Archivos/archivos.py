import os

#LECTURA DE ARCHIVOS

#Ruta absoluta = La ruta completa de su archivo
# C:/archivos de programa/rockstar games/gta v/gtav.exe

#Ruta relativa = Es donde estoy parado
#gtav.exe
#gta v/gtav.exe

#RUTA ABSOLUTA
#/Users/marianofernandez/Desktop/ARCHIVOS/archivo.txt

#RUTA RELATIVA
#archivo.txt

archivo = open("archivo.txt","r")

print(archivo.closed)#FALSE

#LEO TODA LA INFORMACION
#texto = archivo.read()
#LEO LOS PRIMEROS 5 CARACTERES
# print(archivo.tell())
# texto = archivo.read(5)
# print(texto)
# print(archivo.tell())
# archivo.seek(0)
# texto_dos = archivo.read(7)
# print(archivo.tell())
# print(texto_dos)
#archivo.seek(9)

# texto = archivo.read()
# print(texto)

#READLINES

# lista_lineas = archivo.readlines()

# print(lista_lineas)

# for linea in lista_lineas:
#     print(linea.strip())

# #READLINE

# archivo.seek(0)

# linea_uno = archivo.readline()
# print(linea_uno.strip("\n"))
# linea_dos = archivo.readline()
# print(linea_dos.strip("\n"))
# linea_tres = archivo.readline()
# print(linea_tres.strip("\n"))
# linea_cuatro = archivo.readline()
# print(linea_cuatro.strip("\n"))
# linea_cinco = archivo.readline()
# print(linea_cinco.strip("\n"))

# for linea in archivo:
#     for letra in linea:
#         print(letra)

#archivo.close()

#print(archivo.closed)#TRUE


#print(os.path.exists("archivo.txt"))

# if os.path.exists("archivo.txt"):
#     archivo = open("archivo.txt","r")
#     #PROCEDIMIENTO
#     print("EL ARCHIVO EXISTE")
#     archivo.close()
# else:
#     #archivo = open("archivo.txt","w")
#     print("EL ARCHIVO NO EXISTE")

