def primer_letra(string):
    if string == "":
        return ""
    else:
        for i in range(0, len(string)):
            if i == 0:
                rta = rta + string[0]
            if string[i] == " ":
                rta = rta + string[i+1]
    return rta

def test_primer_letra():
    assert primer_letra("Tobias Maggiori") == "TM"

# prueba
def test():
    hola = 1

