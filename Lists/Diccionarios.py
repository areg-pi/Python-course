# DICCIONARIOS
'''
            Coleccion donde los elementos tambien se guardan desordenados y la principal caracteristica
            es que tienen 2 elementos por posicion (clave y valor). No puede haber claves duplicadas.
            A cada clave se le asigna un valor, el cual se imprime al llamar a la clave.
            Pueden incluir todo tipo de elementos, listas, tuplas u otros diccionarios.
'''

diccionario = {"azul":"blue", "rojo":"red", "verde":"green"}
dicc = {"Gera":[22, 1.83], "Olha":{"edad":20, "estatura":1.60}}         # Diccionario con diccionario dentro

diccionario["amarillo"] = "yellow"                  # Agregar un nuevo elemento (desordenado)
diccionario["azul"] = "BLUE"                        # Modificar un elemento
del(diccionario["rojo"])                        # Eliminar un elemento

print(dicc)

equipo = {10:"Paulo", 11:"Douglas", 7:"Cristiano"}          # Clave de tipo entero y valor tipo string

print(equipo[7])                                            # Se debe utilizar la clave para imprimir su valor, no la posicion
print(equipo.get(4, "No existe jugador con ese número."))   # Buscar un valor y desplegar texto si no se encuentra
print(10 in equipo)                                         # Buscar clave en un diccionario
print(equipo.keys())                                        # Imprimir solo las claves del diccionario
print(equipo.values())                                      # Imprimir solo los valores de las claves del diccionario
print(equipo.items())                                       # Imprimir claves y su respectivo valor del diccionario
                                                            # dentro de tuplas
print(len(equipo))                                          # Elementos del diccionario
print(equipo.clear())                                       # Limpiar todo el diccionario