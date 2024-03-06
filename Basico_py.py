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
print("Se precenta el arreglo con el dato que  colocaste")
for i in range(0, 5):
    print(arr[i])
"""Otra manera de agregar datos al arreglo se utiliza insert pero este es mas especifico 
con el echo de que lo coloca en un punto especifico por ejemplo: """
arr.insert(1,n)
print("Se precenta el arreglo con el dato con el numero que nos dio en la pocision 1")
for i in range(0, 6):
    print(arr[i])
"""Para eliminar se utiliza remove pero este elimina el primer elemnto que 
coincida con el dato por ejemplo: """
print("Se elimina el numero que nos diste en su primera aparcion")
arr.remove(n)
for i in range(0, 5):
    print(arr[i])
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
print("Se precenta la fucion de 2 arreglo")
arr.extend(arr2)
for i in range(0, 10):
    print(arr[i])
"""Para eliminar el ultimo dato del areglo se utiliza pop"""
print("Se elimino el ultio dato del arreglo")
arr.pop()
for i in range(0, 9):
    print(arr[i])
"""Revese se utiliza para invertir el orden de la lista"""
print("Se invierte el orden del arreglo")
arr.reverse()
for i in range(0, 9):
    print(arr[i])
"""Sort se uliza para ordenar la lista y se ade oreden acendente o decendente"""
print("Se ordena el arrglo")
arr.sort()
for i in range(0, 9):
    print(arr[i])
#Diccionarios 
"""Un diccionario en python es lo  mismo que un map en c++ dos datos en 
donde uno funciona de indice y el otro es valor"""
print("Se muestra el dato en la pocision A")
dic = {"A":20, "B":30}
print(dic["A"])
"""Para eliminar un valor del dccionario se usa del"""
del dic["A"]
#Ciclos for
print("Ciclo for en con 2 parametros")
for i in range(0, 10):
    print(i)
"""En caso de colocar solo un valor la variable se iniciiara en 0 por defceto"""
print("ciclo con un solo paramero")
for i in range(4):
    print(i)
"""En estos ciclos tambien podemos definir de cuanto e cuanto 
queremos que auoente la varible indeice"""
print("Ciclo for con 3 parametros")
for i in range(0,10,2):
    print(i)
"""En los iiterables no tiene una funcion .size como en otros leguanjes pero 
los ciclos se adaptan a los iterables"""
for i in arr:
    print(i)
"""Con los dicionarios funciona diferente ya que contiene 2 datos estos se
 muestras con el .values"""
dic2 = {"a":20, "b":40}
print("Se precentan los valore del diiconario")
for i in dic2.values ():
    print(i)
"""Para imprimir ambos valores se necesita hacer lo siguiente"""
print("Se presenta los items del diccionario")
for i, j in dic2.items():
    print(i , j)
#Ciclos while
"""Sintaxis de while"""
print("Se precenta el ciclo while")
m = 0
while m < 10:
    print(m)
    m+=1
