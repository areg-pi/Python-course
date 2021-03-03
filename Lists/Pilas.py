# PILAS (stacks)
'''
            Son estructuras de datos de tipo LIFO (Last Input, First Output)
            Se simulan mediante listas
'''

pila = [1,2,3]

pila.append(4)                              # Agregar elementos al final de la pila
pila.append(5)
print(pila)

n = pila.pop()                              # Sacar y guardar el ultimo elemento de la pila
print(f"Sacando el elemento {n}")

print(pila)





