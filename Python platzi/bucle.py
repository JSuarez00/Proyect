def run():
    LIMITE = 1000
    contador= 0
    pontecia_2= 2**contador
    while pontecia_2<LIMITE:
        print("la pontencia de 2 elevado al " + str(contador) + "es igual a " + str( pontecia_2))
        contador=contador+1
        pontecia_2=2**contador



if __name__=="__main__":
    run()
