from utils.system_utils import limpiar_pantalla

from controllers.gestor_habitaciones import Gestor_Habitacion
from controllers.gestor_clientes import Gestor_Clientes
from controllers.gestor_reservas import Gestor_Reservas
from controllers.gestor_pagos import Gestor_Pagos

from database.hotel import Hotel



hotel = Hotel()
habitacion = Gestor_Habitacion(hotel)
cliente =  Gestor_Clientes(hotel)
reservas = Gestor_Reservas(hotel)
pagos = Gestor_Pagos(hotel)



# ---------------------------------------------------------------------


def menu():

    opciones = {
        "1": ("Registrar habitación", habitacion.registrar_habitacion),
        "2": ("Registrar cliente", cliente.registrar_cliente),
        "3": ("Crear reserva", reservas.crear_reserva),
        "4": ("Procesar Pago", pagos.registrar_pago),
        "5": ("Cancelar reserva", reservas.cancelar_reserva),
        "6": ("Editar Reserva", reservas.editar_reserva),
        "7": ("Editar Habitación", habitacion.editar_habitacion),
        "8": ("Ver historial de Reservas", reservas.historial_reservas),
        "9": ("Ver historial de Pagos", pagos.historial_pagos),
        "10": ("Ver habitaciones del sistema", habitacion.mostrar_habitaciones),
        "0": ("Salir", None)
    }


    while True:
        print("\n=== Menú Principal ===")

        #Imprime la clave y la descripcion
        for k, (desc, _) in opciones.items():
            print(f"{k}. {desc}")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print(" Saliendo del sistema...")
            break
        
        #busca la opcion y ejecuta la funcion que contiene
        accion = opciones.get(opcion)
        if accion:
            limpiar_pantalla()
            accion[1]()
        else:
            print(" Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

  