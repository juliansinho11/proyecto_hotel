from models.cliente import Cliente

class Gestor_Clientes:
    def __init__(self, hotel):
        self.hotel = hotel
    
    def validar_cliente(self):
        while True:
            try:
                nombre = input("Ingrese el nombre: ")
                documento = int(input("Ingrese el numero de documento: "))
            except ValueError:
                print("Entrada inválida. Debe ingresar un número entero.\n")
                continue
            numero_valido = [ h for h in self.hotel.clientes if h.documento == documento]
            if len(numero_valido) > 0:
                print("El cliente ya esta registrado, intente nuevamente...")
                continue
            return nombre, documento

    def registrar_cliente(self):
        print("\n------------------------")
        print("Registrar Cliente:")
        print("------------------------")
        nombre, documento = self.validar_cliente()
            
        correo = input("Ingrese su Correo: ")
        id_cliente = len(self.hotel.clientes)
        nuevo = Cliente(id_cliente, nombre, documento, correo)
        self.hotel.clientes.append(nuevo)
        print("Cliente registrado exitosamente")

