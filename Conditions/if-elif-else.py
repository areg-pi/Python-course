
###############################################
a = int(input("Digite un numero: "))
b = int(input("Digite otro numero: "))

if (a%2 == 0) and (b%2 == 0):
    print("Ambos numeros son pares.")
elif (a%2 == 0) and (b%2 != 0):
    print("Solo a es par.")
elif (a%2 != 0) and (b%2 == 0):
    print("Solo b es par.")
else:
    print("Los numeros son impares.")
###############################################

letra = input("\n\nEscriba una letra: ")
letra = letra.lower()                              # lower() para minusculas y upper() para mayusculas

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'i' or letra == 'u':
    print("Es vocal.")
else:
    print("No es vocal.")
