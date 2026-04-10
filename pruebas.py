from gettext import find
NyA="Maria Garcia"
esp=NyA.find(" ")
IA=esp+2
A=str(NyA[esp+1:IA])
IN=str(NyA[0])
iniciales=IN+A
print(iniciales)
usuariop = str(NyA.lower())
usuario = usuariop[esp+1:]+"."+usuariop[:esp]
print(usuario)
print(F"Cantidad de a: {NyA.count("a")}")
print(f"Codigo secreto: {NyA[::-1].upper()}")


