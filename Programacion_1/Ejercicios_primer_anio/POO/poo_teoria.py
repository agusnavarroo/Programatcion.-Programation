import random

class Alumno : # Creamos la clase alumno, siempre en estilo UpperCammeCase
    #legajo
    #nombre
    #apellido        # Todos estos son los atributos
    #edad
    #nota_final

    def __init__(self,legajo:int,nombre:str,apellido:str,edad:int,nota_final:int) -> None: # Esto es el constuctor, construye el objeto a partir de la clase, entre parentesis se colocan los atributos
        # Todos los atributos, con self.nombre_atributo
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota_final = nota_final

    def mostrar(self) : # Esto es el metodo, que es lo mismo que el comportamiento
        print(self.nombre)

    def rendir_parcial(self) :
        nota_aleatoria = random.randint(0,10)
        self.nota_final = nota_aleatoria

alumno_uno = Alumno(1000,"Mariano","Fernandez",30,8) # Creo el objeto alumno 1
alumno_dos = Alumno(1001,"Luis","Tulis",20,7) # Creo el objeto alumno 2

alumno_uno.mostrar() # Los objetos se van a mostrar con un metodo del mismo
alumno_dos.mostrar()
alumno_uno.rendir_parcial()