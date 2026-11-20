class Animal: 
    def __init__(self,nombre):
        self.nombre = nombre 

    def hacer_ruido(self):
        print("Hacer ruido")
class Perro(Animal):
    def __init__(self, nombrePerro,razaPerro,colorPerro):
        self.nombre = nombrePerro
        self.raza = razaPerro
        self.color = colorPerro
    def hacer_ruido(self):
        print("Guau")


class Gato(Animal):
    def __init__(self, nombreGato, razaGato):
        self.nombre = nombreGato
        self.raza = razaGato

    def hacer_ruido(self):
        print("Miau")

perro=Perro("Winnie","Teckel","Blanco")
gato=Gato("Tera","Común")

perro.hacer_ruido()
gato.hacer_ruido()