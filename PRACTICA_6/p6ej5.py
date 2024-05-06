def primeras_letras(string):
    """
    string es una cadena de palabras separadas por un espacio.
    primeras_letras : String String -> String
    Dado un String devuelve una cadena resultante de concatenar
    la primer letra de cada palabra que contenga el String dado.
                        Ejemplos:
    primeras_letras("Alegebra y Geometria Analitica") == "AyGA"
    primeras_letras("Universal Serial Bus") == "USB"
    primeras_letras("Analisis Matematico") == "AM"
    """
    if string == "":
        rta = ""
    else:
        rta = string[0] 
    for i in range(0, len(string)):
        if string[i] == " ":
            rta = rta + string[i+1]
    return rta

def test_primeras_letras():
    assert primeras_letras("Alegebra y Geometria Analitica") == "AyGA"
    assert primeras_letras("Universal Serial Bus") == "USB"
    assert primeras_letras("Analisis Matematico") == "AM"

def primeras_a_mayus(string):
    """
    string es una cadena de palabras separadas por un espacio.
    primeras_a_mayus : String -> String
    Dado un string convierte a mayuscula la primer
    letra de cada palabra y luego lo devuelve.
    Ejemplos:
    primeras_a_mayus("república argentina") == "República Argentina"
    primeras_a_mayus("") == ""
    primeras_a_mayus("argentina") == "Argentina"
    """
    if string == "":
        rta = ""
    else:
        rta = string[0].upper() + string[1:] #Convierte a Mayus la primer letra del String.
    for i in range(0, len(string)):
        if rta[i-1] == " ":
            rta = rta[:i] + rta[i].upper() + rta[i+1:] #Convierte a Mayus toda letra posterior a un espacio.
    return rta

def test_primeras_a_mayus():
    assert primeras_a_mayus("república argentina") == "República Argentina"
    assert primeras_a_mayus("") == ""
    assert primeras_a_mayus("argentina") == "Argentina"