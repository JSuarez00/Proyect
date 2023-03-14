def fibo(n):
    if n == 0 or n == 1:
        return n
    else:return fibo(n-1) + fibo (n-2)

def run():
   num=int(input("escribe el recorrido de la secuencia fibo deseada: "))
   fibonaci=fibo(num)
   print(fibonaci)
   


if __name__=="__main__":
    run()