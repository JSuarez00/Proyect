def palidromo(palabra):
    palabra.replace(" ","")
    palabra.lower()
    palabra_invertida=palabra[::-1]
    if palabra==palabra_invertida:
        return True
    else:
        return False


def run ():
    palabra= input("escribe un palabra: ")
    es_palimedro= palidromo(palabra)
    if es_palimedro==True:
        print("Es palidromo ")
    else:
        print("no es palidromo")


if __name__ == "__main__":
    run()