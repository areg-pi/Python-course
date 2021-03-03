'''
                EJERCICIO 1 LISTAS
                Escriba un programa donde tenga una lista y que elimine los elementos repetidos
                Por ultimo mostrar la lista
'''

lista = ["Olha", 4, 7, 17, True, 4, "Olha"]
print(lista)

conjunto = set(lista)
print(conjunto)

lista = list(conjunto)
print(lista)

# MISMO EJERCICIO EN UN LINEA RESUELTO   ---------------------------------------------------------------

lista = ["Olha", 4, 7, 17, True, 4, "Olha"]

lista = list(set(lista))
print(lista)