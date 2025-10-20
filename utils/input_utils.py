# Importa la clase datetime para trabajar con fechas.
from datetime import datetime

def pedir_fecha(prompt):
    """
    Solicita al usuario una fecha con el formato AAAA-MM-DD y la valida.
    
    El bucle continúa hasta que el usuario introduce una fecha en el formato correcto.

    Args:
        prompt (str): El mensaje que se muestra al usuario para pedir la fecha.

    Returns:
        datetime: Un objeto datetime con la fecha que ingresó el usuario.
    """
    while True:
        # Pide al usuario que ingrese una fecha y elimina espacios en blanco.
        raw = input(prompt).strip()
        # Verifica si la entrada está vacía.
        if raw == "":
            print("Error: la fecha no puede estar vacía. Use el formato AAAA-MM-DD, por ejemplo 2025-10-07.")
            continue # Vuelve al inicio del bucle.
        try:
            # Intenta convertir la cadena de texto a un objeto de fecha.
            dt = datetime.strptime(raw, "%Y-%m-%d")
            return dt # Devuelve el objeto de fecha si el formato es correcto.
        except ValueError:
            # Si el formato es incorrecto, muestra un error.
            print(f"Error: formato de fecha inválido ('{raw}'). Debe usar AAAA-MM-DD, por ejemplo 2025-10-07.")

def pedir_entero():
    """
    Solicita al usuario que ingrese un número entero y lo valida.

    Returns:
        int: El número entero ingresado por el usuario.
    """
    while True:
        try:
            # Pide al usuario un valor y lo convierte a entero.
            numero = int(input("Ingrese el valor deseado: "))
        except ValueError:
            # Si la conversión falla, muestra un error.
            print("Entrada inválida. Debe ingresar un número entero.\n")
            continue
        return numero # Devuelve el número si es válido.

def pedir_indice_cliente(clientes):
    """
    Solicita al usuario el ID de un cliente y valida que exista.

    Args:
        clientes (list): La lista de clientes para validar el índice.

    Returns:
        int: El índice válido del cliente en la lista.
    """
    while True:
        try:
            # Pide el ID del cliente y lo convierte a entero.
            idx = int(input("Ingrese el ID del cliente: "))
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.\n")
            continue
        # Verifica si el índice está dentro del rango válido de la lista de clientes.
        if idx < 0 or idx >= len(clientes):
            print(f"El ID {idx} no existe. Intente nuevamente...\n")
            continue

        return idx # Devuelve el índice si es válido.

def pedir_indice_habitacion(habitaciones, filtro):
    """
    Solicita el ID de una habitación y valida su existencia y estado.

    Args:
        habitaciones (list): La lista de habitaciones del hotel.
        filtro (list): Una lista de estados válidos para la habitación (ej. ["Disponible"]).

    Returns:
        int: El índice válido de la habitación.
    """
    while True:
        try:
            # Pide el ID de la habitación.
            idx = int(input("Ingrese el ID de la habitación: "))
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.\n")
            continue
        # Valida que el índice esté en el rango correcto.
        if idx < 0 or idx >= len(habitaciones):
            print(f"El ID {idx} no existe. Intente nuevamente...\n")
            continue
        habitacion = habitaciones[idx]
        # Verifica si el estado de la habitación coincide con el filtro.
        if habitacion.estado not in filtro:
            print("La habitacion no está Disponible. Intente con otra.\n")
            continue
        return idx # Devuelve el índice si todas las validaciones son correctas.

def pedir_indice_reserva(reservas, filtro):
    """
    Pide el ID de una reserva y valida su existencia y estado.

    Args:
        reservas (list): La lista de reservas del hotel.
        filtro (list): Una lista de estados válidos para la reserva (ej. ["Activa"]).

    Returns:
        int: El índice válido de la reserva.
    """
    while True:
        try:
            # Pide el ID de la reserva.
            idx = int(input("Ingrese el ID de la reserva: "))
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.\n")
            continue
        # Valida que el índice esté en el rango correcto.
        if idx < 0 or idx >= len(reservas):
            print(f"El ID {idx} no existe. Intente nuevamente...\n")
            continue
        reserva = reservas[idx]
        # Verifica si el estado de la reserva coincide con el filtro.
        if reserva.estado not in filtro:
            print("La reserva no está activa. Intente con otra.\n")
            continue
        return idx # Devuelve el índice si es válido.

 


    
    
