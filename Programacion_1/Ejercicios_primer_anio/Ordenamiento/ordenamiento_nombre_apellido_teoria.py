matriz = [["Nombre A","Apellido A"],
          ["Nombre A","Apellido B"],
          ["Nombre B","Apellido B"],
          ["Nombre A","Apellido B"],
          ["Nombre C","Apellido C"],
          ["Nombre Z","Apellido A"]          
          ]

def ordenar_alumnos(matriz, ascendente: bool, prioridad: bool):
    if prioridad == True:
        #si prioridad = TRUE, primera busqueda = APELLIDO, sino NOMBRE
        #prioridad = TRUE (prioridad al nombre)
        primera_busqueda = 1
        segunda_busqueda = 0
    else:
        primera_busqueda = 0
        segunda_busqueda = 1

    
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz)):
            if ascendente == True:
                if(matriz[i][primera_busqueda] > matriz[j][primera_busqueda]):
                    aux = matriz[i]
                    matriz[i] = matriz[j] 
                    matriz[j] = aux

                if(matriz[i][segunda_busqueda] > matriz[j][segunda_busqueda]):
                    aux = matriz[i]
                    matriz[i] = matriz[j] 
                    matriz[j] = aux
            else:
                if(matriz[i][primera_busqueda] < matriz[j][primera_busqueda]):
                    aux = matriz[i]
                    matriz[i] = matriz[j] 
                    matriz[j] = aux

                if(matriz[i][segunda_busqueda] < matriz[j][segunda_busqueda]):
                    aux = matriz[i]
                    matriz[i] = matriz[j] 
                    matriz[j] = aux
                
def mostrar_lista(matriz):
    for i in range(len(matriz)):
        mensaje = ""
        for j in range(len(matriz[i])):
            mensaje += f"{matriz[i][j]} "
        print(mensaje)

ordenar_alumnos(matriz, True, False)
print("-------")
mostrar_lista(matriz)