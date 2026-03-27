def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    Gasto=float(input("gasto"))
    Ingreso=int(input("recibido"))
    print("Ingresar gasto:") #de acá a abajo tiene que ser todo print
    print(Gasto)
    print("Dinero recibido")
    print(Ingreso)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    vuelto_p=(Ingreso-Gasto)
    print(int(vuelto_p))
    print("Centavos:")
    print(int(vuelto_p*100-(int(vuelto_p)*100)))
change()






