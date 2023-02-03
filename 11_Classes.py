# CLASSES
"""
Sirve para agrupar funciones relacionadas
Los nombres se definen con camel case, mayúsculas al comienzo de cada palabra sin guiones.
Deben poder recibir parametros.
Es un objeto, que define una entidad, a su vez con características intrinsecas 
"""

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    # Definimos un contructor de clase con __init__:
    def __init__(self, name, surname, alias = "Sin alias"):
        #le asignamos a self una propiedad name, y le asignamos un valor
        self.full_name = f"{name} {surname} ({alias})"
       
    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = Person("Fabri", "Rovaretti", "Flakira")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Daniel", "Rovaretti", "Chapulin")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Franco Rovaretti (Rova)"
print(my_other_person.full_name)