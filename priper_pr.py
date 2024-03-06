#Las variables en python no se necesitan declarar el tipo, el mismo interprete se encarga de definirlas  
s = "Hola mundo"
n = len(s)
print(s)
print(n)
#Manipuacion de los strings
print(s[5])
#Suub string
print(s[1:9])
#Sub string con saltos de caracteres 
print(s[1:9:2])
s2 = "apoco si"
#Funcion que hace que la primera letra de la cadena se haga mayuscula
print("Esta es la cadena Original: "+s2)
print("Esta es la cadena despues de capitalize: "+s2.capitalize())
#Funcion find te regresa un entero el cual indica en que caracter se encuentra alguna cadena
print("Esta es la cadena despues de find: "+s2[s2.find("oco"):])
#Funcion index indica la cantidad de veces que aparece un caracter en un string 
n = s2.index("o")
print(n)
#Funciones con "is" se enfocan es retornar verdadero o falso basandose si una cadena solo tiene ciertas caracteristicas
s3 = "A1B2C3"
print("La cadena A1B2C3 solo tiene caractere alfanumericos?")
print(s3.isalnum())
#lectura de variable con input puro esto regresa lo que le ingresamos como una cadena de caracteres pero no como variable
x = input("Teclea un numero ")
print(x)
#Lectura de con input pero retornando el tipo de variable
x1 =int(input("Ingresa un numero y se le sumara 2 "))
print(x1 + 2)
#Operadores diferentes a otros lenguajes
"""Uno de los operadore es "//" este se usa para hacer una divición entre dos enteros, 
en la cual el resultado de decimal pero lo arroja en entero"""
x3 = 50//3
print(x3)
"""Otro de los operadores que se usan es "**" el caul se usa para los exponentes"""
x4 = 2**3
print(x4)
#Operadores logicos AND, OR y NOT
"""La prioridad en el codigo es NOT, AND, OR""" 
a = 1
b = 2
c = 3
d = 4
print("Se checa si 1 es mneor a 2 y si 3 es menor 4")
print((a<b)and (c<d))
"""Los operadore ">" "<" "==" ">=" "<=" "!=" se pueden usar para ver si una cadena es alfanmericamente mas grande a otra"""
print("Se checa si la cadena A es menor a la cadena AB ")
print("A" <"B")
#Uso de condicionales
if a<b:
    a+=b
    print("Resultado del if")
    print(a)
#sintaxis de if
"""if a<b:"""
#sintaxis de else if
"""elif"""
#sintaxis de else
"""else:"""
"""Todos estos se manejan con tabulaciones en ves de llaves 
los cierres de estos es regresando del tabulador"""
#Arreglos / listas en python
arr=[1,2,3,4]
print("Se presenta la pocisión 1 del arreglo")
print(arr[1])
"""Para agregar datos al final del arreglo se utliza lo siguiente"""
n = int(input("Tecle un numero para agregar a el arreglo: "))
arr.append(n)
"""Otra manera de agregar datos al arreglo se utiliza insert pero este es mas especifico 
con el echo de que lo coloca en un punto especifico por ejemplo: """
arr.insert(1,n)
"""Para eliminar se utiliza remove pero este elimina el primer elemnto que 
coincida con el dato por ejemplo: """
arr.remove(n)
"""Para saber si un dato existe en el arreglo se utiliza in este comando regresa un dato bool"""
print(n in arr)
"""Para encontrar la posición de un dato dentro de un arreglo usamos index """
print("El dato que nos diste se encuntra en la pocision ")
print(arr.index(n))
"""Para contar cuantas veces aparece un elento en el arreglo se usa count"""
print("Se muestra la cantidad de veces que parece el numero que ingreso en eñ arreglo")
print(arr.count(n))
"""Para fucionar arreglos se utiliza enxtend"""
arr2 =[2,3,4,5,6]
arr.extend(arr2)
"""Para eliminar el ultimo dato del areglo se utiliza pop"""
arr.pop()
"""Revese se utiliza para invertir el orden de la lista"""
arr.reverse()
"""Sort se uliza para ordenar la lista y se ade oreden acendente o decendente"""
arr.sort()
