class Cliente:
    def __init__ (self, id, nombre, documento, correo):
        self.id = id
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
    
    def __str__(self):
        return f"ID: {self.id} || Nombre: {self.nombre} || N° documento: {self.documento} || Correo: {self.correo}"