#Para declarar variables glovales se colocan antes de las funciones 
l = 20 
def hola():
    print("Hola")
    print("Esto es una variable global" , l)
def holar(n):
    for i in range(0, n):
        print("hola")
def suma(n,m):
    return n+m
def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
hola()
x = int(input("Numero de saludos: "))
holar(x)
print("Se imprime el valor retornado por una funcion que suma 2 y 5")
print(suma(2,5))
x2 = int(input("Tecle un nnumero para hacer fibonacci "))
print(fibo(x2))