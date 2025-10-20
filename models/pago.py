class Pago:
    def __init__(self, reserva, metodo, monto):
        self.reserva = reserva
        self.metodo = metodo
        self.monto = monto
    
    def __str__(self):
        return f"""
                ================= FACTURA DE PAGO =================
                HOTEL PRIVAGO
                Cliente: {self.reserva.cliente.nombre}
                Documento: {self.reserva.cliente.documento}
                Habitación: {self.reserva.habitacion.numero} ({self.reserva.habitacion.tipo})
                ---------------------------------------------------
                Fechas: {self.reserva.fecha_ingreso.strftime('%d/%m/%Y')} - {self.reserva.fecha_salida.strftime('%d/%m/%Y')}
                Método de pago: {self.metodo.upper()}
                Monto pagado: ${self.monto:,.2f}
                Total tarifa: ${self.reserva.tarifa:,.2f}
                Estado de pago:  Aprobado
                ===================================================
                """