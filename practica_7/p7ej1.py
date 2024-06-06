# Representacion de una carta de bajara francesa:
# Una carta de baraja francesa es: (valor, palo)
# Donde valor puede ser cualquier elemento de la siguiente tupla:
# (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
# Y palo puede ser cualquier elemento de la siguiente tupla:
# ('corazones', 'diamantes', 'tréboles', 'picas')
# De no cumplise estas condiciones, el elemento no es una carta de baraja francesa.

def crear_carta(valor, palo):
    valores_validos = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
    palos_validos = ('corazones', 'diamantes', 'tréboles', 'picas')

    if valor in valores_validos:
        if palo in palos_validos:
            retorno = (valor, palo)
        else:
             retorno = f"Palo inválido: {palo}. Los palos válidos son: {palos_validos}"
    else:
        retorno = f"Valor inválido: {valor}. Los valores válidos son: {valores_validos}"
    return retorno

