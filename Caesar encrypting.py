
# Caesar encrypting

alphabet = 'abcdefghijklmnñopqrstuvwxyz'
rotkey = int(input('Ingrese la clave de 1 a 27: '))

caracter = input('Ingrese un caracter: ')
position = alphabet.find(caracter)
print(position)

newPosition = (position + rotkey) % 27
newCaracter = alphabet[newPosition]

print('El nuevo caracter es: ', newCaracter)