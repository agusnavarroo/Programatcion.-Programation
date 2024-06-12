#ESCRITURA

# archivo = open("archivo.txt","r")

# archivo.write("HOLA MUNDO\n")
# archivo.write("HOLA DIVISION 314")

# lista = ["Hola\n","Division 314\n","Mariano"]
# print(lista)
#lista = ["Hola\n","Division 314\n","Mariano"]
# diccionario = {"nombre":"Mariano","apellido":"Fernandez"}
# archivo.writelines(diccionario.values())
# archivo_dos = open("archivo2.txt","r")
# archivo.writelines(archivo_dos)
# archivo.close()
# archivo_dos.close()

# print(archivo.tell())
# texto = archivo.read()
# print(texto)
# print(archivo.tell())
# archivo.seek(5)
# texto_dos = archivo.read()
# print(texto_dos)

# archivo.close()

with open("archivo.txt","a") as archivo:
    #MANIPULAMOS EL ARCHIVO
    # texto = archivo.read()
    # print(texto)
    archivo.write("Hola Division 314")

# archivo_dos.close()
print(archivo.closed)