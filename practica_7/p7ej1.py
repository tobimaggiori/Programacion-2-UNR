def crear_carta(valor, palo):
    # Listas de valores y palos válidos
    valores_validos = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    palos_validos = ['corazones', 'diamantes', 'tréboles', 'picas']
    
    # Validación del valor y el palo
    if valor not in valores_validos:
        raise ValueError(f"Valor inválido: {valor}. Los valores válidos son: {valores_validos}")
    if palo not in palos_validos:
        raise ValueError(f"Palo inválido: {palo}. Los palos válidos son: {palos_validos}")
    
    # Retorna la carta como una tupla
    return (valor, palo)