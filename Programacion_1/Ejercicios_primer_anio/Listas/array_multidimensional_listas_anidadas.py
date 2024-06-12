# lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lista_ciudades = [["Madrid","Barcelona","Sevilla"],["Londres","Manchester","Liverpool"]]
# lista_usuarios = [["Mariano",40], ["Luis",30] , ["German",60]]

# print(lista_anidada[1])

# lista_anidada = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# lista_usuarios = [ ["Mariano",40], ["Luis",30] , ["German",60]]
# lista_ciudades = [["Madrid","Barcelona","Sevilla"], ["Londres","Manchester","Liverpool"]]

# print(lista_anidada[1][2]) #Accedo al elemento de la segunda fila en la última columna, o sea al número 6
# print(lista_anidada[2][1]) #Accedo al elemento de la tercer fila en la segunda columna, o sea al número 8
# print(lista_usuarios[0][0]) #Accedo al elemento de la primer fila en la primer columna o sea a Mariano
# print(lista_usuarios[1][1]) #Accedo al elemento de la segunda fila en la segunda columna o sea a la edad de Luis
# print(lista_usuarios[2]) #Accedo a la tercer fila y obtengo la información total de la misma, por ejemplo toda la
# # Información de German
# print(lista_ciudades[0][1])#Barcelona
# print(lista_ciudades[1][0])#Londres

lista_usuarios = []
for i in range(5): #FILAS
    lista_usuario = [] #Creo la lista de la info de un solo usuario
    dato = int(input("Ingrese el dato: "))
    lista_usuario.append(dato)

lista_usuarios.append(lista_usuario)
print(lista_usuarios)