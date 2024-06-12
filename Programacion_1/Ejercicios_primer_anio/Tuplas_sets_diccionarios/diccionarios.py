#DICCIONARIOS

usuario = { 'nombre':'Mariano',
        "apellido":"Fernandez",
        'edad':80,
        'genero':'Masculino'
}

# print(usuario)
# print(usuario['nombre'])
# print(usuario['apellido'])
#print(usuario["lalala"])
# print(usuario.get("lalala"))
# print(usuario.get("nombre"))
# print(usuario.get("lalala","El dato no existe"))

# print(usuario.keys())
# print(list(usuario.keys()))

# print(usuario.values())
# print(list(usuario.values()))

# print(usuario.items())
# print(list(usuario.items()))#ME LO CONVIERTE EN LISTA DE TUPLAS

# matriz_diccionario = list(usuario.items()) 
# for i in range(len(matriz_diccionario)):
#     matriz_diccionario[i] = list(matriz_diccionario[i])#LO CONVIERTE A MATRIZ

# print(matriz_diccionario)

# for clave in usuario:
#     #print(clave) POR DEFECTO ACCEDE A LAS CLAVES
#     print(usuario[clave])
    
# for i in range(len(usuario)):
#     print(usuario[i])

# for valor in usuario.values():
#     print(valor)

# print(usuario)
# elemento_eliminado = usuario.pop("apellido")
# print(usuario.pop("apellido","No se puede eliminar este dato porque no existe"))
# print(usuario)
# print(f"Elemento eliminado: {elemento_eliminado}")

# #CLEAR
# print(usuario)
# usuario.clear()
# print(usuario)

#UPDATE

# diccionario = {"dni":44444444,"peso":80.5,"nombre":"Jose"}

# print(usuario)
# usuario.update(diccionario) #AGREGA, MODIFICA Y TAMBIEN CONCATENA DICCIONARIOS
# print(usuario)

# print(usuario)
# usuario['peso'] = [2,5,10]
# print(usuario)

#DICCIONARIOS ANIDADOS

# domicilio = {"calle":"Mitre", "numero":777,"localidad":"Avellaneda"}

# usuario = { 'nombre':'Mariano',
#         "apellido":"Fernandez",
#         'edad':80,
#         'genero':'Masculino',
#         'domicilio':domicilio
# }

# print(usuario["domicilio"]["localidad"])
