
# LISTAS
'''
            Son como los vectores/arreglos en otros lenguajes y pueden tener todo tipo de elementos.

'''

lista = [ 10, 'Mar', 1, True, 'Jue', [1, 4, 72], 1]

lista.append(6)             # Agrega un elemento al siempre final
lista.append("Gera")

lista.insert(3, False)      # Agrega un elemento en la posicion indicada, 3 en este caso

lista.extend([1,2,3,4,5])

print(lista[:])                 # Imprime todos los elementos de la lista con :
print(len(lista))               # Cantidad de elementos de la lista
print(17 in lista)              # Ver si un valor esta en la lista
print(lista.index('Jue'))       # Indice en el que se encuentra un elemento
print(lista.count(1))           # Cuantas veces aparece un valor en una lista

lista.pop(4)              # Elimina un elemento de la lista (dando el indice); borra el ultimo si no se especifica
lista.remove(1)           # Elimina el valor especificado de la lista
lista.clear()             # Limpia/borra toda la lista
lista.reverse()           # Voltear la lista
lista = [ 1,2,3,4,5]*3    # Copiar/multiplicar los elementos de forma seguida
lista.sort()              # Ordenar elementos ascendentemente
lista.sort(reverse=True)              # Ordenar elementos descendentemente

print(lista[:])

if (10 in lista) == True:
    print("Si esta")
else:
    print("No esta")