from models.pago import Pago

from utils.print_utils import mostrar_reservas_activas
from utils.input_utils import pedir_indice_reserva, pedir_entero


class Gestor_Pagos:
    def __init__(self, hotel):
        self.hotel = hotel
    

    #Verifica que se haya elegido un metodo de pago y que lo pagado coincida con la tarifa
    def registrar_pago(self):

        #Vefica que haya reservas previas
        if not mostrar_reservas_activas(self.hotel.reservas):
            print("\nError: No hay reservas activas para procesar.")
            return

        index_reserva = pedir_indice_reserva(self.hotel.reservas, ["Activa"])
        reserva = self.hotel.reservas[index_reserva]

        metodo = input("Elija el meotodo de pago (efectivo, tarjeta): ").lower()
        while  metodo not in [ "efectivo", "tarjeta"]:
            print("Has ingresado mal el metodo de pago. Intentalo de nuevo")
            metodo = input("Elija el meotodo de pago (efectivo, tarjeta): ").lower()

        #validar que sea un pago completo
        if metodo == "efectivo":
            monto = pedir_entero()
            while monto != reserva.tarifa:
                print("falta dinero, ingrese de nuevo el valor!!")
                monto = pedir_entero()
        else:
            monto = reserva.tarifa

        pago = Pago(reserva, metodo, monto)
        reserva.pago = "Aprobado"
        reserva.estado = "Finalizado"
        reserva.habitacion.estado = "Disponible"
        self.hotel.pagos.append(pago)
        print(pago)



    #Imprime el historial de pagos realizados
    def historial_pagos(self):
        pagos_realizados = [p for p in self.hotel.pagos]
        if pagos_realizados:
            print("\n == Historial de pagos == ")
            for p in pagos_realizados:
                print(p)
        else:
            print("\n == Error: No hay pagos realizados == ")

