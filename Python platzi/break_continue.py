def run ():
    LIMITE=100
    contador=0
    

    while contador < LIMITE:
        contador=contador+1
        if contador % 2 != 0:
            continue
        print(contador)


    # for contador in range(1,100):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    # for i in range(9999):
    #     if i==(9852):
    #         break
    #     print(i)


  # frase= input("escribe una frase: ")


    # for i in frase:
    #     if i == "i":
    #         break
    #     print(i)


        
if __name__=="__main__":
    run()