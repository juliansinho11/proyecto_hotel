class Habitacion:
    def __init__(self, id, numero):
        self.id = id
        self.numero = numero
        self.estado = "Disponible"

    def __str__(self):
        return f"ID: {self.id} || Nº: {self.numero} || Estado: {self.estado}"

class Sencilla(Habitacion):
    def __init__(self, id, numero):
        super().__init__(id, numero)
        self.tipo = "Sencilla"
        self.costo = 10000
    
    def __str__(self):
        return f"{super().__str__()} || Tipo: {self.tipo} || Costo/noche: $ {self.costo}"


class Doble(Habitacion):
    def __init__(self, id, numero):
        super().__init__(id, numero)
        self.tipo = "Doble"
        self.costo = 30000
    
    def __str__(self):
        return f"{super().__str__()} || Tipo: {self.tipo} || Costo/noche: $ {self.costo}"
    

class Suite(Habitacion):
    def __init__(self, id, numero):
        super().__init__(id, numero)
        self.tipo = "Suite"
        self.costo = 90000
    
    def __str__(self):
        return f"{super().__str__()} || Tipo: {self.tipo} || Costo/noche: $ {self.costo}"