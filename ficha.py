def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    neim=input("Introduce el nombre completo del alumno: ")
    NyA=neim.title().strip()
    meil=input("Introduce el correo del alumno: ")
    correo=meil.lower().strip()
    nota1=input("Introduce la nota 1: ")
    nota2=input("Introduce la nota 2: ")
    nota3=input("Introduce la nota 3: ")
    print("="*24)
    print("    FICHA DEL ALUMNO")
    print("="*24)
    print(f"Nombre: {NyA.title()}")
    print(f"Email: {correo}")
    print(f"Caracteres en nombre: {len(NyA)}")
    esp = NyA.find(" ")
    IA = esp + 2
    A = str(NyA[esp + 1:IA])
    IN = str(NyA[0])
    iniciales = IN + A
    print(f"Iniciales: {iniciales.upper()}")
    usuariop=NyA.lower()
    usuario=usuariop[esp+1:]+"."+usuariop[:esp]
    print(f"Usuario: {usuario}")
    print(f"Email valido: {'@' in correo}")
    arren = correo.find("@")
    dominio=correo[arren+1:]
    print(f"Dominio: {dominio}")
    print(F"Nombre para archivo: {NyA.replace(' ', '_')}")
    print(F"Cantidad de a: {NyA.count('a')}")
    print(f"Codigo secreto: {NyA[::-1].upper()}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    nota1_int=int(nota1)
    nota2_int=int(nota2)
    nota3_int=int(nota3)
    print(f"Suma: {nota1_int + nota2_int+nota3_int}")
    print(f"Promedio: {(nota1_int + nota2_int + nota3_int) / 3}")
    print(f"Promedio entero: {(nota1_int + nota2_int + nota3_int) // 3}")
    print("="*24)


