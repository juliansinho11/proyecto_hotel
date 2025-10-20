# Define la clase Reserva para representar una reserva en el hotel.
class Reserva:

    def __init__(self, id_reserva, cliente, habitacion, fecha_ingreso, fecha_salida):
        """
        Inicializa un objeto de reserva.

        Args:
            id_reserva (int): El identificador único para la reserva.
            cliente (Cliente): El objeto cliente que realiza la reserva.
            habitacion (Habitacion): El objeto habitación que se reserva.
            fecha_ingreso (datetime): La fecha de inicio de la reserva.
            fecha_salida (datetime): La fecha de finalización de la reserva.
        """
        self.id_reserva = id_reserva  # Identificador único de la reserva.
        self.cliente = cliente  # Objeto Cliente asociado a la reserva.
        self.habitacion = habitacion  # Objeto Habitacion asociado a la reserva.
        self.fecha_ingreso = fecha_ingreso  # Fecha de inicio de la reserva.
        self.fecha_salida = fecha_salida  # Fecha de fin de la reserva.
        self.estado = "Activa"  # Estado inicial de la reserva.
        self.tarifa = 0  # Tarifa total, se calcula después.
        self.pago = "Pendiente"  # Estado del pago, inicialmente pendiente.

    def _recalcular(self):
        """
        Calcula la tarifa total de la estancia.

        La tarifa se basa en el número de noches multiplicado por el costo por noche de la habitación.
        Maneja excepciones si el cálculo falla, estableciendo la tarifa en 0.0.
        """

        try:
            noches = (self.fecha_salida - self.fecha_ingreso).days
            if noches < 0:
                noches = 1
            self.tarifa = noches * float(self.habitacion.costo)
        except Exception:
            self.tarifa = 0.0

    # Devuelve una representación en cadena de la reserva con sus detalles.
    def __str__(self):
        try:
            # Formatea las fechas para una mejor visualización.
            desde = self.fecha_ingreso.date()
            hasta = self.fecha_salida.date()
        except Exception:
            desde = str(self.fecha_ingreso)
            hasta = str(self.fecha_salida)
        
        # Retorna una cadena formateada con todos los detalles de la reserva.
        return (f"| ID: {self.id_reserva} | Cliente: {self.cliente.nombre} "
                f"| Habitación: {self.habitacion.numero} | Desde: {desde} hasta {hasta} "
                f"| Dias: {(self.fecha_salida - self.fecha_ingreso).days} | Tarifa/noche: ${self.habitacion.costo} | Total: ${self.tarifa} "
                f"| Estado: {self.estado} | Pagada: {self.pago}")