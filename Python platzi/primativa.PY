def es_primado(numero):
      contador=0
      for i in range(1,numero+1):
        if i == 1 or i == numero:
            continue
        if  numero % i == 0:
                contador+=1
        if contador == 0:        
                return True
        else:
             return False        

def run():
    numero=int(input("escribe un numero: "))
    if es_primado(numero)==True:
        print("es primado ")
    else:
        print("no es primado ")    
    
   


if __name__=="__main__":
    run()