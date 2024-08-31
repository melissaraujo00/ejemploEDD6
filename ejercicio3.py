print("Menu de opciones")
print("\n 1- Ver la fecha de incripcion del ciclo I 2025")
print("\n 2- Ver la fecha de inicio del ciclo I 2025")
print("\n 3- Ver la fecha de finalizacion del ciclo I 2025")
print("\n 4- Salir")
while True:
    opc = int(input("Digite la opcion que deseas ver: "))

    if opc == 1:
        print("La fecha de incripcion del ciclo I 03/01/25 a 12/01/25")
    elif opc == 2:
        print("La fecha de inicio del ciclo I es 13/01/25")
    elif opc == 3:
        print("La fecha de finalizacion del ciclo I es el 15/06/25")
    elif opc == 4:
        print("Salio del programa")
        break
    else: 
        print("Ingrese un valor valido")
    