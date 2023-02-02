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
    def __init__(self, name, surname, dni = "indocumentadx"):
        #le asignamos a self una propiedad name, y le asignamos un valor
        self.full_name = f"{name} {surname} DNI N°: {dni}"
       
    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = Person("Fabri", "Rovaretti", 33270596)
print(my_person.full_name)
my_person.walk()

