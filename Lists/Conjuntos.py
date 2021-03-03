# Conjuntos
'''
            Coleccion donde los elementos estan desordenados y no puede haber duplicados.
            Pueden almacenar todo tipo de datos
            No pueden contener listas
'''
conjunto = set()                     # Conjunto vacío con la función set(). Pyhton consideraría poner c = {} como
                                     # un diccionario vacío

conjunto = {1,2,3, 'Hi', 4.31, 1,2,3}       # Tambien se pueden abrir con llaves, pero se puede confundir con diccionarios
                                            # La diferencia es que aqui no hay dos puntos como en diccionarios
                                            # Los valores no se duplican, se guardan una vez y se imprimen una vez
conjunto.add(5)                 # Agrega un valor en donde sea, ya que es una colleccion de datos desordenados
conjunto.add('Helou')

conjunto.discard(3)             # Elimina el elemento indicado
conjunto.clear()                # Vacía el conjunto

print(5 in conjunto)            # Buscar un valor en el conjunto
print(5 not in conjunto)        # Ver si un valor no está en el conjunto
print(conjunto)

#  OPERACIONES CON CONJUNTOS

c1 = {1,2,3}
c2 = {3,4,5,6}
c3 = {2,1,3}
c4 = {1,4,6,2,3}

print(c1 == c2)                 # Checar si dos conjuntos son iguales
print(c1 == c3)                 # En conjuntos no importa el orden, habrá un True si tienen los mismos elementos
print(len(c2))                  # Cantidad de elementos

c_union = c1 | c2               # Unión de dos conjuntos. Aquí no funciona con +, pero en listas sí
c_inter = c1 & c2               # Intersección de dos conjuntos (elementos que hay en ambos conjuntos)
c_dif = c1 - c2                 # Diferencia de conjuntos (elementos de c1 que no estan en c2)
c_dif_sim = c1 ^ c2             # Diferencia simétrica (elementos que hay en c1 y c2 pero no en ambos)

print(c1.issubset(c4))          # Preguntar si c1 es subconjunto de c4 (si c1 esta contenido en c4)
print(c4.issuperset(c1))        # Preguntar si c4 es superconjunto de c1 (si en c4 estan los elementos de c4)
print(c1.isdisjoint(c4))        # Preguntar si c4 y c1 son disconexos (si no comparten ningun elemento)

c5 = frozenset({1,5,7,9})       # Función frozenset() para hacer un conjunto inmutable, no se podrá añadir ni eliminar
