import datetime
from funciones import *
# fecha_hoy = datetime.date.today() para obtener la fecha de hoy
# fecha_formato_perzonalizado = fecha_hot.strftime("%d/%m/%Y") para cambiar el formato a dia/mes/año

registro_mascotas = [
    ["12345678", "Luna", 3, "Perro", "Hembra", 8.5, "01/05/2024", "Vacunación anual"],
    ["23456789", "Max", 7, "Gato", "Macho", 5.2, "28/04/2024", "Control de pulgas"],
    ["34567890", "Kiwi", 1, "Dragón", "Hembra", 88000, "02/05/2024", "Recorte de alas"],
    ["45678901", "Rocky", 5, "Perro", "Macho", 12.1, "30/04/2024", "Revisión dental"],
    ["56789012", "Coco", 2, "Gato", "Hembra", 4.8, "03/05/2024", "Desparasitación"]
]

while(True):
    opcion = int(input("Elija una opción: "))
    match opcion:
        # ALTA
        case 1:
            registro = registrar_mascota()
            registro_mascotas.append(registro)
            print(registro_mascotas)
        case 2:
            # MODIFICACION
            mostrar_lista_anidada(registro_mascotas)
            indice = buscar_mascota(registro_mascotas)
            if indice != None :
                print("Se encontro la mascota")
                actualizar_mascota(indice,registro_mascotas)
                print(registro_mascotas)
            else :
                print("No se encontro la mascota")
        case 3:
            mostrar_lista_anidada(registro_mascotas)
        case 4:
            calcular_promedio_edad(registro_mascotas)
        case 5:
            calcular_promedio_peso(registro_mascotas)
        case 6:
            contar_perros(registro_mascotas)
        case 7:
            mostrar_mascota_mas_registrado(registro_mascotas)
        case 8:
            print("Saliendo del sistema.")
            break
    

