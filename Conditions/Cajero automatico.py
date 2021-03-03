saldo = 1000.0
n = 0.0

print("\tINICIO")
print("\t1. Ingresar dinero en la cuenta.")
print("\t2. Retirar dinero de la cuenta.")
print("\t3. Mostrar dinero disponible.")
print("\t4. Salir.")

while True:
    option = input("Seleccione una opción y presione Enter: ")
    if option == '1':
        n = float(input("Escriba la cantidad a ingresar: "))
        saldo += n
        print(f"Saldo actual: {saldo:.2f}")
    elif option == '2':
        n = float(input("Escriba la cantidad a retirar: "))
        if n > saldo:
            print("No cuenta con esa cantidad.")
        else:
            saldo -= n
            print(f"Saldo actual: {saldo:.2f}")
    elif option == '3':
        print(f"Saldo actual: {saldo:.2f}")
    elif option == '4':
        print("\nHa salido. Gracias por su preferencia.")
        break
    else:
        print("Opción inválida.")