
# For Loop

for i in [1,2,3,4, "Gera"]:               # Se imprime Hola mundo la misma cantidad de elementos que la lista
    print("Hola mundo")

for i in [1,2,3,4,5]:
    print(i, end="")                      # Usar end="" para sustituir por \n (default)

print("\n")
for i in [1,2,3,4, "Gera"]:
    print(f"Elemento: {i}")

lista = [1,4,"man"]                      # Se puede usar la variable de la lista, tuplas, conjuntos
for i in lista:
    print(i)

str = "Olha"
for i in str:
    print(f"{i}")

#                               FOR CON DICCIONARIOS
diccionario = {"Gera":22, "Olha":20, "Luis":12}
for i in diccionario:
    print(f"Elemento: {i}")              # En este caso se imprime solo la clave del elemento del diccionario

for i in diccionario:
    print(f"Elemento: {diccionario[i]}") # En este caso se imprime solo la clave del elemento del diccionario

for clave, valor in diccionario.items():
    print(f"{clave} ---> {valor}")

