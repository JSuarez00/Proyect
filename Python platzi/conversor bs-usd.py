def conversor (valor_dolar,moneda):
    bolivar = float (input("¿cuantos " + moneda + " tienes?: "))
    
    ### operacion matematica .,
    dolares = bolivar / valor_dolar
    dolares = round (dolares,2)
    dolares = str(dolares)
    print("tienes $ "+ dolares +" dolares")

menu="""
"Bienvenido al converso de monedas a dolares💲"

1- Bolivares venezolanos
2- peso colombianos
3- peso mexicanos

"""
opcion =int(input(menu))

if opcion==1:
    conversor(25000,"Bolivares venezolanos" )
    
    
elif opcion==2:
    
    conversor(3875,"pesos colombianos" )
   
elif opcion==3:
    conversor(64," pesos MEXICANOS" )
else:
    print("ingresa una opcion correcta, por favor")



