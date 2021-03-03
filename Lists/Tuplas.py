
# TUPLAS
'''
        A diferencia de las listas, las tuplas ya no se pueden modificar durante el programa;
        ademas, se usan parentesis
        Pueden tene todo tipo de elementos, hasta una lista.
        No se puede usar pop() o append(), por ejemplo.
        Sirven mucho para hacer busquedas y consumen menos memoria que las listas
'''
tupla = (4, 'Hola', 6.78, [1,2,3], 4)

print(tupla[1:3])
print(5 in tupla)                       # Busca el valor en la tupla y regresa True or False
print(tupla.index('Hola'))              # Regresa el indice en el que se encuentra el valor (tiene que estar a huevs)
print(tupla.count(4))                   # Regresa la cantidad de veces que aparece este valor en la tupla
print(len(tupla))                       # Cantidad de elementos de la tupla

# Transformar tupla en lista y viceversa

lista = list(tupla)                     # list() convierte la tupla en lista y la guarda en una variable indicada
print(lista)

nueva_tupla = tuple(lista)              # tuple() convierte la lista en tupla y la guarda en una variable indicada
print(nueva_tupla)