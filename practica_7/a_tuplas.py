# Una tupla es (elemento, elemeneto, elemento), formalmente tupla = elemento, elemento, elemento
# (elemento) no es una tupla, (elemento,) sí es una tupla.

# Iteración sobre tuplas:
def imprimeValoresTupla(tupla):
    for elemento in tupla:
        print(elemento)

# ImprimeValoresTupla((2, 4, 6))
# 2
# 4
# 6

# Version recursiva de la funcion ImprimeValoresTupla(tupla):
def imprimeValoresTuplaRec(tupla):
    if tupla != ():
        print(tupla[0]) # imprime el primer elemento de la tupla.
        imprimeValoresTuplaRec[tupla[1:]] # llama a la funcion en el resto de la tupla.

# ImprimeValoresTuplaRec((2, 4, 6))
# 2
# 4
# 6

# DIFERENCIAS DE LAS TUPLAS CON LAS LISTAS
# Las tuplas no poseen mecanismos de modificacion, ionserción ni eleiminación.
# Ademas las tuplas no son mutables, es decir, son inmutables por lo que sus
# valores no se pueden modificar una vez creada y tienen un tamaño fijo.

# ¿PARA QUE SIRVEN LAS TUPLAS?

