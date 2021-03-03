
a = int(input('Digite un número: '))
b = int(input('Digite otro número: '))

if (a%2 == 0) and (b%2 == 0):
    print('Los números son par.')

elif (a%2 != 0) and (b%2 != 0):
    print('Los números son impares.')

else:
    if a % 2 == 0:
        print('El primer número es par')
    else:
        print('El primer número es impar')

    if b % 2 == 0:
        print('El segundo número es par')
    else:
        print('El segundo número es impar')