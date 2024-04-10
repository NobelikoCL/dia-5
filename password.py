import getpass

while True:
    # Solicitar al usuario que ingrese una contraseña
    password = getpass.getpass("Ingrese su password: ")

    # Comprobar si la longitud de la contraseña es menor a 6 o mayor a 6
    if len(password) < 6:
        print("El password es demasiado corto")
    elif len(password) > 6:
        print("El password es demasiado largo")
    else:
        print("Su contraseña tiene los parámetros correctos")
        break

    retry = input("¿Desea ingresar nuevamente la contraseña? (s/n): ")
    if retry.lower() != 's':
        break