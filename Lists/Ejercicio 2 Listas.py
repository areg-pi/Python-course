'''
                EJERCICIO 2 LISTAS
                Escriba un programa con 2 listas, que a continuacion se creen las sig. listas:
                    - Lista de palabras que aparecen en las dos listas
                    - Lista de palabras que aparecen en la primera lista, pero no en la segunda
                    - Lista de palabras que aparecen en la segunda lista, pero no en la primera
                    - Lista de palabras que aparecen en ambas listas
'''
lista1 = ["Hi", "Bye", 1, 4, 7, "Mei", "Akane", "we", 5, 7, 1]
lista2 = ["Hello", 2, 7, "Bye", "wey", 4, 1, 1, "Akane", "we"]

# Eliminando elementos repetidos al convertirse en conjuntos
a = set(lista1)
b = set(lista2)

union = list(a | b)                                      # Regresandolos a lista al hacer las operaciones
print(f"Elementos de las dos listas: {union}")

soloA = list(a - b)
print(f"Elementos de primera lista pero no segunda: {soloA}")

soloB = list(b - a)
print(f"Elementos de segunda lista pero no primera: {soloB}")

interseccion = list(b & a)
print(f"Elementos de ambas listas: {interseccion}")