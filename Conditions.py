#Conditions

import math

r = float(input('Ingrese el radio del círculo: '))

area = math.pi * r**2
perimetro = 2 * math.pi * r

if r >= 10:
    print(f'El área es {area:.3f} y el perímetro {perimetro:.3f}')

elif 0<r<10:
    print(f'El área con r menor a 10 es {area:.3f} y el perímetro {perimetro:.3f}')

else:
    print('El radio no es válido.')