import random as rd


def run():
    numero_aleatorio = rd.randint(1, 100)
    win=str.upper("en hora buena Ganaste !! ")
    numero= int(input("Adivina un numero del 1 al 100: "))
    while numero != numero_aleatorio:
        if numero < numero_aleatorio:
            print("Escoje un numero mayor ")
        else:
            print("Busca un numero mas pequeño ")
        numero= int(input("escoje otro numero "))
    print(win)        


if __name__=="__main__":
    run()