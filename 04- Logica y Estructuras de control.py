# ------------------------------ OPERADORES ------------------------------

# Son símbolos o conjunto de símbolos que realizan una operación específica en uno o más operandos

# Tipos de Operadores
    # Aritméticos
    # De Comparación
    # Lógicos
    # De Asignación
    # De Pertenencia
    # De identidad

# Aritméticos
    # + para sumar
    # - para restar
    # + para multiplicar
    # / para dividir
    # // para dividir en entero (floor division)
    # % resto o módulo (modulus)
    # ** exponenciación

from argparse import BooleanOptionalAction
from operator import truediv
from typing import final


a = 7
b= 4
c= a // b # división de enteros
d= a % b # resto o módulo
e= a ** b

print (c)
print (type(c))
print (d)
print (e)

# De Asignación
# = asignación 

x= 10 # asignación

y= 5
sumatorio = 4

y += sumatorio #9
y += sumatorio #13
y += sumatorio #17
y += sumatorio #21

print (y)

z= 10
restatorio = 2

z -= restatorio #8
z -= restatorio #6
z -= restatorio #4
z -= restatorio #2

print (z)

d= 10
aMultiplicar = 2

d *= aMultiplicar #20
d *= aMultiplicar #40
d *= aMultiplicar #80
d *= aMultiplicar #160

print (d)

e= 100
aDividir= 2

e /= aDividir #50
e /= aDividir #25
e /= aDividir #12,5
e /= aDividir #6,25 #También se puede dividir por entero con la //

print (e)

f= 2
aExponer= 2
f **= aExponer #4
f **= aExponer #16
f **= aExponer #256
f **= aExponer #65536
print (f)

# De Comparación

# == nos sirve para comparar igualdad, devuelve un booleano
# ! es la negación (ampliaremos)
# != nos sirve para comparar diferencia
# > mayor
# < menor
# >= mayor o igual
# <= menor o igual

x= 5
y= 5
z= 6

print (x == y) # True
print (x == z) # False
print (x != z) # True
print (x > z) # False
print (x < z) # True
print (x <= z) # True

# Lógicos

# and nos va a devolver verdadero si y solo si ambas afirmaciones son verdaderas
# or nos va a devolver verdadero si alguna de las dos afirmaciones es verdera
# not nos devolvera lo opuesto al valor que siga

x = 5

booleano= x>3 and x<10
booleano1= x>3 or x<10
booleano2= x<3 and x<10

print(booleano2)

booleano3 = not x == 0
booleano4 = not x != 0

print(booleano3)
print(booleano4)

# De Identidad (para números y textos)
#is
#is not 

ab = 5
cd = 4

booleanoid = ab is cd #Es lo mismo que poner ==

print (booleanoid)

de= 10
fg= 10

booleanoisnot = de is not fg # es lo mismo que el !=

print (booleanoisnot)

# De Pertenencia
#in
#not in

texto= "En este texto pondremos algunas teconologías: Python, R, Django y TensorFlow"

print ("Python" in texto) #True
print ("Excel" not in texto) #True
print ("TensorFlow" not in texto) #False
minuscula = texto.lower()
print (texto.lower())
print ("python" in texto.lower())

print ("python" in minuscula)

# ------------------------------ ESTRUCTURAS DE CONTROL ------------------------------

# Una estructura de control es un bloque de código que permite controlar el flujo de ejecución de un programa.
# Estas estructuras determinan qué instrucciones se ejecutarán y en qué orden basándose en condiciones específicas.

    # Estructuras de decisión (condicionales): permiten ejecutar cierto bloque de código si se cumple una condición, de lo contrario se ejecuta otro bloque de código
    # Bucles (loops): permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición o hasta que se vuelva falsa.
    # Estructuras de control de excepciones: permiten manejar errores o excepciones de un programa, controlando cómo se manejan los errores cuando ocurren durante la ejecución.

# Condicionales:
''' if condicion_1:
    # Código a ejecutar si la condicion_1 es verdadera
elif condicion_2:
    # Código a ejecutar si la condicion_2 es verdadera
else:
    # Código a ejecutar si ninguna de las condiciones anteriores es verdadera

    # Condiciones ternarias: Son una forma concisa de expresar una estructura condicional en una sola linea:
    """ Se utilizan principalmente para asignar valores a una variable en función de una condición"""

valor_si_condicion_verdadera if condicion else valor_si_condicion_falsa
# Ejemplo
x=10
resultado= "positivo" if x > 0 else "negativo"

print (resultado)

# Bucle WHILE

while condicion:
    # Código a ejecutar mientras la condición sea verdadera

# Bucle FOR

for indice in range (cantidad):
    # Código a ejecutar en cada iteración

# Manejo de Excepciones

try:
    # Código que pueda generar una excepción
except tipodeexcepción as nombre_variable:
    # Código para manejar la excepción
finally:
    # Código que siempre se ejecuta, es OPCIONAL

# Palabras Clave
'''
# BREAK
for i in range (5):
    if i == 3:
        break
    print (i) #Se espera: 0,1,2

# CONTINUE
for i in range (5):
    if i == 3:
        continue
    print (i) # Se espera: 0,1,2,4

# PASS
x = 10
if x > 5:
    pass # No hace nada, solo sirve como marcador de posición. Es para que cuando no tenemos algo definido no se rompa el código y siga de largo
else:
    print () #x es menor o igual a 5)
        
# If, Elif, Else

x=10

if x>0:
    print("x es un número positivo")
elif x<0:
    print("x es un número negativo")
else: 
    print("x es igual a 0")

visa= True
pasaporte= False

if visa or pasaporte:
    print("puedes ingresar a cualquier pais")
elif pasaporte and not visa:
    print("puedes ingresar solo a los países que no requieren visa")
else:
    print("Debes conseguir la documetación antes de viajar")

edad=40

if edad < 18 or edad > 60:
    if edad < 18:
        print("no tienes edad suficiente para entrar a la disco")
    elif edad > 60:
        print("por cuestiones de seguridad no se permite ingreso a mayores de 60 años")
elif edad > 18 and edad < 60:
    print("Puedes ingresar a la disco") 

"""#En el caso anterior no necesita que lleve else"""

# While

contador= 0

while contador < 5:
    print("el contador es:",contador)
    contador += 1
print(contador)
while contador < 10:
    contador += 1
    print("el contador es:",contador)

contador=0
limite=5
sumatoria=0

while contador <= limite:
    sumatoria+= contador
    contador+=1

print("la suma de los números hasta:", limite, "es:",sumatoria)

# For

for i in range (5):
    print(i)

for i in range (1,11):
    print(i)

for i in range (2,11,2):
    print(i)

for i in range (0,9,2):
    if i == 2:
        print("paso por el número 2")
    else:
        print("no es número 2, es el número:",i)

# Try, Except, Finally

# Manejo de la división por cero

a = 10
b = 0
#c = a/b
# print(c) error división por 0

a = 10
b = 0
try: #intenta hacer esto e imprimi el resultado
    resultado= a/b
    print(resultado)
except ZeroDivisionError:#si se da este error devolver tal mensaje
    print("No se puede dividir por 0")
finally:#mensaje apesar de que dió error
    print ("ccc") 

# Break

contador= 0
while contador < 10:
    print(contador)
    if contador == 5:
        break
    contador += 1
print(contador)

# Continue

contador= 0
while contador < 10:
    print(contador)
    contador += 1
    if contador == 5:
        continue
    print ("imprimir por cada vuelta")
    #si aca pusieramos el contador += 1 de la linea de arriba queda en un constante bucle. Crtrl+C me ayuda a frenar este bucle
print(contador)

for i in range (10):
    if i % 2 == 0: 
        continue
    print (i) #acá se puede ver lo números impares ya que anteriormente puse que el resto es "0" pero si coloco resto "1" me duevuelve pares  

# Pass

edad=19

if edad > 18:
    print("Puedes ingresar a esta institución")
elif edad == 18: # si tiene 18 de edad no va hacer nada el sistema y permite continuar al else
    pass
else:
    print("no tienes edad suficiente para entrar aquí")

