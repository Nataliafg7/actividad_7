#1. Defina una clase Elemento usando el decorador @dataclass que contenga lo siguiente

#Un atributo nombre de tipo str
#Un método especial para soportar la operación de igualdad == que permita comparar dos objetos de la clase Elemento indicando si el nombre es igual.·


from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def igual (self, otro):
        if isinstance(otro, Elemento):
            return self.nombre == otro.nombre
        return False

#ejemplo:
# el_1 = Elemento("sol")
#el_2 = Elemento("estrellas")

#if el_1 == el_2:
    #print("Los nombres son iguales.")
#else:
    #print("Los nombres son diferentes.")


#2. Defina una clase Conjunto que contenga lo siguiente

#Un atributo de instancia que representa la lista de objetos de la clase Elemento, inicialice el atributo como una lista vacía.
#Un atributo de instancia nombre que contiene el nombre del conjunto. Inicialice dicho atributo a partir de un parámetro dado en el método inicializador.
#Un atributo de clase contador que lleve registro del número de instancias creadas. Incremente en uno el valor de dicho atributo en el método inicializador.
#Un atributo “privado” __id al cual se le asigna el valor actual del atributo de clase contador al momento de la inicialización. Defina una propiedad de solo lectura para dicho atributo (aquí deberá consultar cómo se define una propiedad de solo lectura en Python).

class Conjunto:
    contador = 0  

    def __init__(self, nombre):
        self.elementos = []  
        self.nombre = nombre  
        Conjunto.contador += 1  
        self.__id = Conjunto.contador 

   


    def id(self):
        return self.__id 



# Ejemplo:
#el_1 = Elemento("sol")
#el_2 = Elemento("estrellas")


#conj_1 = Conjunto("conjunto_1")
#conj_2 = Conjunto("conjunto_2")

#print(f"ID de conjunto1: {conj_1.id}")
#print(f"ID de conjunto2: {conj_2.id}")


#Un método de instancia contiene, el cual recibe como parámetro un objeto de la clase Elemento y retorna un valor bool indicando si el conjunto contiene ya un elemento con el mismo nombre.
#Un método de instancia agregar_elemento, el cual recibe un objeto de la clase Elemento como parámetro y lo agrega a la lista de elementos si no está contenido ya en el conjunto (utilice el método anterior para verificar)
#Un método unir que recibe otro conjunto como parámetro y agrega sus elementos a la lista de elementos del objeto actual en el que se invoca el método. Tenga en cuenta que un conjunto no puede tener elementos repetidos. Implemente también esta operación por medio de un método especial para soportar el operador +.
#Un método de clase intersectar que recibe dos conjuntos como parámetros y retorna un nuevo conjunto con los elementos de la intersección de los conjuntos dados. Recuerde que la intersección de dos conjuntos está conformada por los elementos que pertenecen a ambos conjuntos. El nombre del conjunto resultante debe ser "<Nombre Conjunto 1> INTERSECTADO <Nombre Conjunto 2>.
#Un método __str__ que retorne una representación legible de un conjunto con el siguiente formato "Conjunto <nombre>: (<nombre elemento 1>, <nombre elemento 2>,...,<nombre elemento n>)"

    def contiene_elemento(self, elemento):
        for elem in self.elementos:
            if elem.nombre == elemento.nombre:
                return True
        return False

    def agregar_elemento(self, elemento):
        if not self.contiene_elemento(elemento):
            self.elementos.append(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        for elem in self.elementos:
            nuevo_conjunto.agregar_elemento(elem)
        for elem in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elem)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto_1, conjunto_2):
        elementos_comunes = []
        for elem1 in conjunto_1.elementos:
            if conjunto_2.contiene_elemento(elem1):
                elementos_comunes.append(elem1)
        nombre_resultante = f"{conjunto_1.nombre} INTERSECTADO {conjunto_2.nombre}"
        nuevo_conjunto = cls(nombre_resultante)
        for elem in elementos_comunes:
            nuevo_conjunto.agregar_elemento(elem)
        return nuevo_conjunto

def __str__(self):
        elementos_str = ", ".join([elem.nombre for elem in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})" 

#jemplo
#el_1 = Elemento("sol")
#el_2 = Elemento("estrellas")
#el_3 = Elemento("constelaciones")

#conjunto_1 = Conjunto("conjunto_1")
#conjunto_2 = Conjunto("conjunto_2")

#conjunto_1.agregar_elemento(el_1)
#conjunto_1.agregar_elemento(el_2)
#conjunto_1.agregar_elemento(el_3)

#conjunto_2.agregar_elemento(el_2)
#conjunto_2.agregar_elemento(el_3)

#print("¿El conjunto_1 contiene sol?", conjunto_1.contiene_elemento(el_1))
#print("¿El conjunto_2 contiene constelaciones?", conjunto_2.contiene_elemento(el_3))

#union = conjunto_1 + conjunto_2
#print("Elementos en la unión de conjunto_1 y conjunto_2:", [elem.nombre for elem in union.elementos])

#interseccion = Conjunto.intersectar(conjunto_1, conjunto_2)
#print("Elementos en la intersección de conjunto_1 y conjunto_2:", [elem.nombre for elem in interseccion.elementos])