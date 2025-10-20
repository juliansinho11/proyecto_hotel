# Importa funciones y clases necesarias de otros módulos.
from utils.print_utils import mostrar_clientes, mostrar_habitaciones_disponibles, mostrar_reservas_activas
from utils.input_utils import pedir_fecha
from utils.input_utils import pedir_indice_habitacion, pedir_indice_cliente, pedir_indice_reserva
from models.reserva import Reserva

# Define la clase para gestionar las reservas.
class Gestor_Reservas:
    """
    Inicializa el gestor con una referencia al hotel.
    Args:
            hotel (Hotel): Una instancia de la clase Hotel que contiene los datos del hotel.
    """
    def __init__(self, hotel):
        self.hotel = hotel

    def crear_reserva(self):
        """
        Crea una nueva reserva en el sistema.

        Solicita la información del cliente, la habitación y las fechas de la reserva.
        Si no hay clientes o habitaciones disponibles, muestra un mensaje de error.
        """
        # Verifica si hay clientes y habitaciones registrados.
        if not self.hotel.clientes or not self.hotel.habitaciones:
            print("\n Error: No hay clientes ni habitaciones registrados. Registre almenos 1 habitacion y un 1 cliente (opcion 1 y 2)")
            return
        print("\n-----------------------------------------------")
        print("Crear Reserva")
        print("-----------------------------------------------")

        # Muestra los clientes y pide al usuario que elija uno.
        mostrar_clientes(self.hotel.clientes)
        index_cliente = pedir_indice_cliente(self.hotel.clientes)
        cliente = self.hotel.clientes[index_cliente]

        # Muestra las habitaciones disponibles y pide al usuario que elija una.
        mostrar_habitaciones_disponibles(self.hotel.habitaciones)
        index_habitacion = pedir_indice_habitacion(self.hotel.habitaciones, ["Disponible"])
        habitacion = self.hotel.habitaciones[index_habitacion]

        # Pide las fechas de inicio y fin de la reserva.
        fecha_inicio = pedir_fecha("Ingrese la fecha inicio (AAAA-MM-DD): ")
        fecha_fin = pedir_fecha("Ingrese la fecha fin (AAAA-MM-DD): ")
        while fecha_inicio >= fecha_fin:
            print("Error: la fecha de inicio debe ser anterior a la fecha de fin.")
            fecha_inicio = pedir_fecha("Ingrese la fecha inicio (AAAA-MM-DD): ")
            fecha_fin = pedir_fecha("Ingrese la fecha fin (AAAA-MM-DD): ")

        # Crea una nueva instancia de Reserva. 
        reserva = Reserva(
            len(self.hotel.reservas), 
            cliente, habitacion, 
            fecha_inicio, 
            fecha_fin
        )
        reserva._recalcular()  # Calcula el costo total de la reserva.
        habitacion.estado = "Ocupada"  # Cambia el estado de la habitación.
        self.hotel.reservas.append(reserva)  # Agrega la reserva a la lista del hotel.
        print(f"Reserva creada correctamente")
    

    def editar_reserva(self):
        """
        Edita una reserva existente.

        Permite al usuario cambiar la habitación, la fecha de entrada y la fecha de salida de una reserva activa.
        """
        if not mostrar_reservas_activas(self.hotel.reservas):
            print("\n Error: No hay reservas activas para editar")
            return 
        
        print("\n-----------------------------------------------")
        print("Modificar Reserva")
        print("-----------------------------------------------")

        # Pide al usuario que elija una reserva activa para editar.
        idx = pedir_indice_reserva(self.hotel.reservas, ["Activa"])
        reserva = self.hotel.reservas[idx]

        # Permite cambiar la habitación de la reserva.
        cambiar_hab = input("Desea cambiar la habitación? (s/n): ").strip().lower()
        if cambiar_hab == "s":
            if not mostrar_habitaciones_disponibles(self.hotel.habitaciones):
                return
            idx_nuevo = pedir_indice_habitacion(self.hotel.habitaciones, ["Disponible"])
            nueva_habitacion = self.hotel.habitaciones[idx_nuevo]
            reserva.habitacion = nueva_habitacion

        # Permite cambiar la fecha de ingreso.
        cambiar_entrada = input("Desea cambiar la fecha de ingreso? (s/n): ").strip().lower()
        if cambiar_entrada == "s":
            nuevo_ingreso = pedir_fecha("Ingrese la Nueva fecha de ingreso: ")
        else:
            nuevo_ingreso = reserva.fecha_ingreso

        # Permite cambiar la fecha de salida.
        cambiar_salida = input("Desea cambiar la fecha de salida? (s/n): ").strip().lower()
        if cambiar_salida == "s":
            nueva_salida = pedir_fecha("Ingrese la Nueva fecha de salida: ")
        else:
            nueva_salida = reserva.fecha_salida

        # Valida que la fecha de inicio sea anterior a la de fin.
        while nuevo_ingreso >= nueva_salida:
            print("Error: la fecha de inicio debe ser anterior a la fecha de fin.")
            nuevo_ingreso = pedir_fecha("Ingrese la Nueva fecha de ingreso: ")
            nueva_salida = pedir_fecha("Ingrese la Nueva fecha de salida: ")
        
        # Actualiza las fechas y recalcula el costo.
        reserva.fecha_ingreso = nuevo_ingreso
        reserva.fecha_salida = nueva_salida
        reserva._recalcular()
        
        print(f"Reserva {reserva.id_reserva} modificada correctamente. Nuevo total: ${reserva.tarifa}")
        return True


    def cancelar_reserva(self):
        """
        Cancela una reserva activa.

        Cambia el estado de la reserva a "Cancelada" y el estado de la habitación a "Disponible".
        """
        if not mostrar_reservas_activas(self.hotel.reservas):
            return 
        print("\n-----------------------------------------------")
        print("Cancelar Reserva")
        print("-----------------------------------------------")

        # Pide al usuario que elija una reserva para cancelar.
        idx_cancel = pedir_indice_reserva(self.hotel.reservas, ["Activa"])

        # Pide confirmación para cancelar.
        confirmado = input("Confirma cancelar la reserva? (s/n): ").strip().lower()
        if confirmado != "s":
            print("Operación cancelada por usuario.")
            return
        reserva = self.hotel.reservas[idx_cancel]
        habitacion = reserva.habitacion
        habitacion.estado = "Disponible"  # La habitación vuelve a estar disponible.

        reserva.estado = "Cancelada"  # Cambia el estado de la reserva.
        print(f"Reserva {reserva.id_reserva} cancelada correctamente.")

    def historial_reservas(self):
        """
        Muestra un historial de todas las reservas, clasificadas por estado (Activas, Canceladas, Pagadas).
        """
        activas = [r for r in self.hotel.reservas if r.estado == "Activa"]
        canceladas = [r for r in self.hotel.reservas if r.estado == "Cancelada"]
        pagadas = [r for r in self.hotel.reservas if r.estado == "Finalizado"]

        # Muestra cada lista de reservas si no está vacía.
        if activas:
            print("\n== Reservas Activas ==")
            for r in activas:
                print(r)
        elif canceladas:
            print("\n== Reservas Canceladas ==")
            for r in canceladas:
                print(r)
        elif pagadas:
            print("\n== Reservas Pagadas ==")
            for r in pagadas:
                print(r)
        else:
            print("\n Error: No hay historial de reservas")
            return