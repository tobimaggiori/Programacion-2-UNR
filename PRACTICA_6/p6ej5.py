def primer_letra(string, rta=""):
    """
    primer_letra : String String -> String

    """
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
    assert primer_letra("Alegebra y Geometria Analitica") == "AyGA"
    assert primer_letra("Universal Serial Bus") == "USB"
    assert primer_letra("Analisis Matematico") == "AM"
