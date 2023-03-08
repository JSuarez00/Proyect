import random 

def pw_generador():
    mayuscula=["A","B","C","D","E","F","G","H","I","J","K","L","LL","M","N","O","P","Q","R","S","T","U","V"]
    minuscula=["a","b","c","d","e","f","g","h","i","j","k","l","ll","m","n","o","p","q","r","s","t","u","v"]
    numero=["1","2","3","4","5","6","7","8","9","O"]
    simbolos=["!","$",";",":",";;","#","€","/"]


    caracteres= minuscula + numero+mayuscula+simbolos

    contrasena=[]

    for i in range(15):
        pw_random=random.choice(caracteres)
        contrasena.append(pw_random) # error =contrasena.


    contrasena="".join(contrasena)

    return contrasena
# def generar_contrasena():
#     mayusculas=["A","B","V"]
#     minusculas=["a","b","g"]
#     simbolos=["!","#","€"]
#     numeros=["1","2","3","4"]

#     carateres=mayusculas+minusculas+simbolos+numeros

#     contrasena=[]

#     for i in range(15):
#         carateres_rango=random.choice(carateres)
#         contrasena.append(carateres_rango)

#     contrasena="".join(contrasena)

#     return contrasena
def run():
    contrasena =pw_generador()
    print ( "tu contraseña es: " + contrasena)
    



if __name__=="__main__":
    run()
