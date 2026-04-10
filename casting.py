def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio=int(input("precio"))
    dto=float(input("dto"))
    numero=int(input("numero"))
    print(f"Precio: {precio}")
    print(f"Descuento: {dto}")
    print(f"Precio con descuento: {precio-dto}")
    print(f"Total: {(precio-dto)*numero}")
