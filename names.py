def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre=input("¿Cómo es SOLO tu nombre?")
    apellido=input("¿Cuál es tu apellido?")
    nya=nombre+" "+apellido
    print(nya.lower())
    print(nya.title())
    print(nya.upper())
    print("\t"+nya.lower())

