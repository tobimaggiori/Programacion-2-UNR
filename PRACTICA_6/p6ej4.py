def contarLetras(string, rta=0):
    """
    contarLetras: String Natural -> Natural
    Cuenta la longitud de la primer (o unica) palabra de un string.
                Ejemplos:
    contarLetras("Tierra Sol Luna") == 6
    contarLetras("") == 0
    contarLetras(" LCC ") == 0
    """
    if string != "":
        aux = True
        i = 0
        while i < len(string) and aux:
            if string[i] != " ":
                rta = rta + 1
                i = i + 1
            else:
                aux = False
    return rta

def test_contarLetras():
    assert contarLetras("Tierra Sol Luna") == 6
    assert contarLetras("") == 0
    assert contarLetras(" LCC ") == 0

def mayoresDeCinco(string, result=0):
    """
    mayoresDeCinco : String Natural -> Natural
    Devuelve la cantidad de palabras de longitud mayor a 5 letras
    que tenga un string de palabras separadas por un espacio.
    Ejemplos:
    mayoresDeCinco("Sol Tierra Magia Computacion") == 2
    mayoresDeCinco("Sol Luna Luz LCC") == 0
    mayoresDeCinco("") == 0
    """
    if string == "":
        return result
    else:
        if contarLetras(string) > 5:
            return mayoresDeCinco(string[contarLetras(string)+1:], result+1)
        else:
            return mayoresDeCinco(string[contarLetras(string)+1:], result)

def test_mayoresDeCinco():
    assert mayoresDeCinco("Sol Tierra Magia Computacion") == 2
    assert mayoresDeCinco("Sol Luna Luz LCC") == 0
    assert mayoresDeCinco("") == 0