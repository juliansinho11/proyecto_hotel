from models.habitacion import Sencilla, Doble, Suite
from utils.input_utils import pedir_indice_habitacion, pedir_entero

class Gestor_Habitacion:
    def __init__(self, hotel):
        self.hotel = hotel
    
    #Vefica que la habitacion no este registrada y devuelve el numero si no esta registrada
    def validar_habitacion(self):
        while True:
            try:
                numero = int(input("Ingrese el numero de la habitación: "))
            except ValueError:
                print("Entrada inválida. Debe ingresar un número entero.\n")
                continue
            numero_valido = [ h for h in self.hotel.habitaciones if h.numero == numero]
            if len(numero_valido) > 0:
                print("La habitacion ya esta registrada, intente nuevamente...")
                continue
            return numero
    
    #Registra una nueva habitación en el sistema solicitando sus datos básicos.
    def registrar_habitacion(self):
        print("\n------------------------")
        print("Registrar Habitación:")
        print("------------------------")

        numero = self.validar_habitacion()

        # Selección del tipo de habitación
        tipo = input("Tipo de habitación (sencilla, doble, suite): ").lower()
        while tipo not in [ "sencilla", "doble", "suite"]:
            print("Has ingresado mal el tipo de habitacion. Intentalo de nuevo")
            tipo = input("Tipo de habitación (sencilla, doble, suite): ").lower()
        
        id_habitacion = len(self.hotel.habitaciones)

        # Crea la instancia correspondiente según el tipo
        if tipo == "sencilla":
            nueva = Sencilla(id_habitacion, numero)
        elif tipo == "doble":
            nueva = Doble(id_habitacion, numero)
        else: 
            nueva = Suite(id_habitacion, numero)

        self.hotel.habitaciones.append(nueva)
        print("Habitación registrada exitosamente")
    
    #Imprime unicamente las habitaciones editables que tienen estado Disponible o Mantenimiento
    def habitaciones_habilitadas_edicion(self):
        disponibles = [h for h in self.hotel.habitaciones if h.estado == "Disponible"]
        mantenimiento = [h for h in self.hotel.habitaciones if h.estado == "Mantenimiento"]
   
        if disponibles:
            print("\n== Habitaciones Disponibles ==")
            for h in disponibles:
                print(h)
        if mantenimiento:
            print("\n== Habitaciones en Mantenimiento ==")
            for h in mantenimiento:
                print(h)
        if not (disponibles or mantenimiento):
            print("\n Error: No hay Habitaciones en el sistema editables")
            return False
        return True
    
    #Edita la informacion de la habitacion seleccionada
    def editar_habitacion (self):

        if not self.habitaciones_habilitadas_edicion():
            return
        
        print("\n------------------------")
        print("Editar Habitación:")
        print("------------------------")

        idx = pedir_indice_habitacion(self.hotel.habitaciones, ["Disponible", "Mantenimiento"])
        habitacion = self.hotel.habitaciones[idx]

        opcion = input("Desea modificar el numero de habitacion s/n: ").strip().lower()
        if opcion == "s":
            nuevo_numero = self.validar_habitacion()
            habitacion.numero = nuevo_numero
            print("numero de habitación actualizado!!")

        opcion = input("¿Desea cambiar el tipo de habitación? (s/n): ").strip().lower()
        if opcion == "s":
            nuevo_tipo = input("Nuevo tipo (sencilla, doble, suite): ").strip().lower()
            while nuevo_tipo not in ["sencilla", "doble", "suite"]:
                print("Tipo inválido. Inténtelo de nuevo.")
                nuevo_tipo = input("Nuevo tipo (sencilla, doble, suite): ").strip().lower()
            habitacion.tipo = nuevo_tipo
            print("Tipo de habitación actualizado!!")

        opcion = input("¿Desea cambiar el estado de la habitación? (s/n): ").strip().lower()
        if opcion == "s":
            nuevo_estado = input("Nuevo estado (Disponible, Ocupada, Mantenimiento): ").capitalize()
            while nuevo_estado not in ["Disponible", "Ocupada", "Mantenimiento"]:
                print("Estado inválido. Inténtelo de nuevo.")
                nuevo_estado = input("Nuevo estado (Disponible, Ocupada, Mantenimiento): ").capitalize()
            habitacion.estado = nuevo_estado
            print("Estado actualizado!!")

        opcion = input("¿Desea modfificar el costo de la habitación? (s/n): ").strip().lower()
        if opcion == "s":
            nuevo_costo = pedir_entero()
            habitacion.costo = nuevo_costo
            print("Costo actualizado!!")

        print(f"\nHabitación {habitacion.numero} modificada correctamente.")

    #Muestra todas las habitaciones clasificadas por sus estados: Disponible, Mantenimiento y Ocupada
    def mostrar_habitaciones(self):
        disponibles = [h for h in self.hotel.habitaciones if h.estado == "Disponible"]
        mantenimiento = [h for h in self.hotel.habitaciones if h.estado == "Mantenimiento"]
        ocupada = [h for h in self.hotel.habitaciones if h.estado == "Ocupada"]
   
        if disponibles:
            print("\n== Habitaciones Disponibles ==")
            for h in disponibles:
                print(h)
        if mantenimiento:
            print("\n== Habitaciones en Mantenimiento ==")
            for h in mantenimiento:
                print(h)
        if ocupada:
            print("\n== Habitaciones Ocupadas ==")
            for h in ocupada:
                print(h)
        if not (disponibles or mantenimiento or ocupada):
            print("\n Error: No hay Habitaciones en el sistema")
            return False
        return True
     