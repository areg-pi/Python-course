# Salidas
name = 'Gerardo'
age = 22

print("Hola, tu nombre es", name, "y tienes", age, "años.")

print("Hola, eres {}, tienes {} años.".format(name, age))    # Shorter way with format

print(f"Hola, te llamas {name}, tienes {age} años.")        # Even shorter

# Entradas

nombre = input("Digite su nombre: ")                # Para guardar strings
numero = int(input("Digite un numero: "))           # Para convertir la str a int
numero2 = float(input("Digite un numero: "))           # Para convertir la str a float

print(f"\nHola, {nombre}.")
print(f"El numero es {numero}.")
print(f"El numero es {numero2:.2f}.")

