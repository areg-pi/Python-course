# PILAS (stacks)
'''
            Son estructuras de datos de tipo FIFO (First Input, First Output)
            Se simulan mediante listas
'''

        # from collections import deque   mediante este import tambien se puede hacer lo siguiente

cola = ["Maria", "Alex", "Gera", "Jelly", "Barry"]
cola.append("Oli")
cola.append("Regina")
print(cola)

# Sacando elementos por el principio de la cola
n = cola.pop(0)
print(f"Atendiendo a {n}")

n = cola.pop(0)
print(f"Atendiendo a {n}")
