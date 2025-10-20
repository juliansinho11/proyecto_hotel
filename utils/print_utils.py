def mostrar_reservas_activas(reservas):
    """
    Muestra una lista de todas las reservas activas en el sistema.

    Args:
        reservas (list): Una lista de objetos de reserva.

    Returns:
        bool: True si hay reservas activas para mostrar, False en caso contrario.
    """
    r_activas = [ r for r in reservas if r.estado == "Activa"] # Filtra la lista de reservas para obtener solo las que tienen el estado "Activa".
    if not r_activas: # Si no se encuentran reservas activas, imprime un mensaje de error y devuelve False.
        print(" \n Error: No hay reservas activas. No se puede realizar la accion...")
        return False
    print("\n------------------------")
    print("Reservas activas en el sistema:")
    print("------------------------")
    # Itera sobre la lista de reservas activas y las imprime.
    for r in r_activas:
        print(r)
    return True # Devuelve True para indicar que se mostraron las reservas.

def mostrar_habitaciones_disponibles(habitaciones):
    """
    Muestra una lista de todas las habitaciones disponibles en el hotel.

    Args:
        habitaciones (list): Una lista de objetos de habitación.

    Returns:
        bool: True si hay habitaciones disponibles para mostrar, False si no hay ninguna.
    """
    h_disponibles = [ h for h in habitaciones if h.estado == "Disponible"] # Filtra la lista de habitaciones para obtener solo las que están "Disponibles".
    if not h_disponibles: # Si no hay habitaciones disponibles, imprime un error y devuelve False.
        print("\n Error: No hay habitaciones disponibles. No se puede realizar la accion...")
        return False
    print("\n------------------------")
    print("Habitaciones Disponibles en el sistema:")
    print("------------------------")
    # Itera sobre la lista de habitaciones disponibles y las imprime.
    for h in h_disponibles:
        print(h)
    return True # Devuelve True, indicando que la operación fue exitosa.

def mostrar_clientes(clientes):
    """
    Muestra una lista de todos los clientes registrados en el sistema.

    Args:
        clientes (list): Una lista de objetos de cliente.

    Returns:
        bool: True si hay clientes para mostrar, False si la lista está vacía.
    """
    if not clientes: # Verifica si la lista de clientes está vacía.
        print("\n Error: No hay Clientes disponibles. No se puede realizar la accion...")
        return False
    print("\n------------------------")
    print("Clientes Disponibles en el sistema:")
    print("------------------------")
    # Itera sobre la lista de clientes y los imprime.
    for c in clientes:
        print(c)
    return True # Devuelve True para indicar que se mostraron los clientes.

