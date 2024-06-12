registro_mascotas = [
    ["12345678", "Luna", 3, "Perro", "Hembra", 8.5, "01/05/2024", "Vacunación anual"],
    ["23456789", "Max", 7, "Gato", "Macho", 5.2, "28/04/2024", "Control de pulgas"],
    ["34567890", "Kiwi", 1, "Dragón", "Hembra", 88000, "02/05/2024", "Recorte de alas"],
    ["45678901", "Rocky", 5, "Perro", "Macho", 12.1, "30/04/2024", "Revisión dental"],
    ["56789012", "Coco", 2, "Gato", "Hembra", 4.8, "03/05/2024", "Desparasitación"]
]

#? Ordenamiento por edad

indice_edad = 2

for i in range(len(registro_mascotas)) :
    for j in range(i + 1, len(registro_mascotas)) :
        if registro_mascotas[i][indice_edad] < registro_mascotas[j][indice_edad] :
            #! Cuando ordeno matrices, no se intercambian las filas y las columnas porque esta mal
            #! Se cambian solo las filas
            aux = registro_mascotas[i]
            registro_mascotas[i] = registro_mascotas[j]
            registro_mascotas[j] = aux
