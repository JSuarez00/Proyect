def msj(mensaje):
    print("Hola")
    print("Como estas")
    print(mensaje)
    print("Adios")

OPCION =int(input("elige una opcion 1,2,3"))
if OPCION== 1:
    msj("elegiste la opcion 1 ")
elif OPCION== 2:
    msj("elegiste la opcion 2 ")
elif OPCION== 3:
    msj("elegiste la opcion 3 ")
else:
    print("elege una opcion validad, por favor")