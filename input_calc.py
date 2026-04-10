def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base=int(input("Ingrese base: "))
    altura=int(input("Ingrese altura: "))
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    area=int(base*altura)
    print(f"Area: {area}")
    perimetro=int(2*base+2*altura)
    print(f"Perimetro: {perimetro}")


