#Concatenar cadenas de caracteres.
#supongamos que queremos crear una cadena que diga:
#aprende a programat con _________.
def run():
    genero=input("escribe tu genero: ")
    verbo1=input("escribe un verbo: ")
    verbo3=input("escribe un otro verbo: ")
    verbo4=input("escribe un ultimo verbo: ")
    abj=input("escribe un abjetivo: ")
    organizacion="Jasz_historiaslocas"
    
    historia=f"Cuentan que, en un antiguo reino, habitaba un\a {genero} que era conocido en todas partes por su gran {verbo4}. Al comienzo solo aconsejaba a sus {verbo1} y amigos cercanos. Sin embargo, su {verbo3} creció tanto que el propio soberano lo llamaba frecuentemente para {verbo4}.Todos los días llegaban muchas {abj} a recibir sus {abj} . Sin embargo, el {verbo3} notó que había varios que iban todas las semanas. Lo peor es que siempre le contaban los mismos {verbo1} y luego escuchaban el mismo  {verbo3} , pero no lo ponían en práctica. Todo se había convertido en un círculo {abj}.Un día, el {verbo1} reunió a todos esos consultantes frecuentes. Luego les contó un chiste tan divertido, que llevó a que casi todos se desternillaran de la risa. Después esperó un rato y volvió a contar el mismo chiste. Siguió contándolo por tres horas. Al final, todos estaban desesperados. Entonces el {verbo1} les dijo ¿por qué no pueden reírse varias veces del mismo chiste , pero sí pueden llorar mil veces por el mismo {verbo1}?" + "\n" "  " + organizacion
    
    
    print(historia)

if __name__=="__main__":
    run()