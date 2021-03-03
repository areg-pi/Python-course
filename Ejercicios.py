#Ejercicios captulo 1


#EJERCICIO 1
a = float(input('Digite el número a: '))
b = float(input('Digite el número b: '))
c = float(input('Digite el número c: '))

expresion = (a**3 * (b**2 - 2*a*c)) / (2*b)

print(f'El resultado es: {expresion}')


#EJERCICIO 2
a = float(input('Digite el número a: '))
b = float(input('Digite el número b: '))

resultado = ((3 + 5*8) < 3) and (((-6*4/3) + 2) < 2) or (a>b)

print(f'El resultado es: {resultado}')


#EJERCICIO 3
a = float(input('Escriba el valor de a: '))
b = float(input('Escriba el valor de b: '))
print("\n")
print(f'El valor de a es {a}'); print(f'El valor de b es {b} \n')
c = a
a = b
b = c
print(f'El valor de a es {a}'); print(f'El valor de b es {b} \n')