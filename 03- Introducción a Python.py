# Variables 
# son contenedores que almacenan datos que pueden cambiar durante la ejecución del programa
# Cada variable tiene un nombre único y un valor asociado
# Para poder asignarle un valor se utilizar el =

mivariable= 'hola'

mivariable ='texto'
print (mivariable)

# No válido: no puede comenzar con número
# 2mivariable= 
# No válido: no se puede usar guiones medios
# mi-variable=
# No válido: no puede comenzar con un espacio
#  mivariable=
# No válido: no se puede usar el simbolo $
# $mi_variable

# ----------------------------TIPOS DE DATOS ----------------------------

# Texto
# - str (cadena de texto)
texto= 'Cadena de caracteres'

# Números 
#int (entero)
número_entero= 10

#float (flotante)
numero_flotante = 10.34

#Secuencia

# - list (lista) -> [colección ordenada y mutable/cambiante]
lista = [1,2,3,4]

#tuple (tupla) -> (colección ordenada pero inmutable/NO cambia)
tupla = (1,2,3,4)

# range (rango) -> [secuencia inmutable de números]
rango = range (0,10)

# mapping (mapeo)

# dict (diccionario)[colección no ordenada de pares clave-valor]
diccionario = {
    "nombre" : "Federico",
    "edad" : 34
}

# set (conjuntos) tenemos 2 tipos de set
# set (conjunto) [colección no ordenada y MUTABLE de elementos únicos que no se pueden repetir]
conjunto = {1,2,3,4}

# frozenset (conjunto INMUTABLE) [idem al anterior pero no se puede modificar]
conjunto_inmutable = frozenset ({1,2,3,4})

# boolean (booleano) [puede ser verdadero o falso]
booleano = True
boolano2 = False

# binary (binario)
# bytes [secuencia inmutable de bytes]
bytes_data = b"datos"

# bytearray (array de bytes) [una secuencia mutable de bytes]
bytearray_data = bytearray (b"datos")

# memoryview (vista de memoria) [Permite acceder a la memoria de objetos de bytes sin hacer una copia]
memoria = memoryview(b"datos")

# none/null (nulos)
# nonetype (nulo) [representa la ausencia de valor o la no definición]
nulo = None

# ---------------------------- CASTEO ----------------------------
# Texto (str)
variable1= "Texto"
variable2 = "123456"
variable3= "Texto123"

# Numéricas
variable4= 10
variable5= 2.5
variable6= 1j

print (type(variable1))# <class 'str'>
print (type(variable2))# <class 'str'>
print (type(variable3))# <class 'str'>
print (type(variable4))# <class 'int'>
print (type(variable5))# <class 'float'>
print (type(variable6))# <class 'complex'>

# Casteo de Texto a Entero
variable7 = int(variable2) #castie la variable 2 en otra variable nueva
print (type(variable7))

# Casteo de Número a Texto
variable8= str(variable4)
print (type(variable8))

# ¿Cómo se castea? (Cambiar el tipo de dato) tipoDeDato ("el dato original")
# con type podemos saber qué tipo de dato es el que estamos manejando
tupla = ("manzana", "pera", "banana")
list = list(tupla)

print (type(list))

# ---------------------------- TIPOS DE DATOS NUMERICOS ----------------------------
x= 1 #int
y= 2.8 #float
z= 2j 

print(type(x))
print(type(y))
print(type(z))

# Casteo de Número (int) a Número (float) y viceversa
x=5
y=float(x)

print(y)
print(type(y))

x=5.5
y=int(x)

print(y)
print(type(y))

# Random

from ctypes.wintypes import HLOCAL
from pickletools import read_int4
import random

x=random.randrange(1,10) #el diez no esta incluído

print(x)

import random

x=random.random()

print(x)
print(type(x))

import random

x=random.randint(1,10) #el diez esta incluído en este randint

print(x)
print(type(x))

# ---------------------------- CADENA DE CARACTERES ----------------------------

string_comillas_simples='hola,mundo!'
string_comillas_dobles="hola,mundo!"
string_comillas_triples='''este texto puede ser
multilinea'''
string_comillas_triple2= """este texto tambien puede ser
multilinea"""

# Slicing: ponemos desde un índice hasta un índice de un caracter NO incluído
txt= "seguimos trabajando con strings"
print(txt[8:19]) #el caracter del final no esta incluído
print(txt[:8]) #si no le pongo nada antes de los ":" me devuelve todo desde el principio
print(txt[8:]) #si no le pongo nada después de los ":" me devuelve todo hasta el final
print(txt[-7:]) #si pongo negativo comienza a contar desde el último caracter
print(txt[-11:-1]) #me devuelve todos los caracteres con excepción de lo que se encuentre en la posición -1

# Mayúscula
txt= 'CUANDO ESCRIBO EN MAYUSCULA TODOS PIENSAN QUE ESTOY GRITANDO'
minuscula= txt.lower() #una forma de poner en minuscula
print(txt.lower()) #otra forma de poner en minuscula
print(minuscula)

# Minúscula
txt= 'melina acordate de esto'
mayuscula= txt.upper() #una forma de poner en mayuscula
print(txt.upper()) #otra forma de poner en mayuscula
print(mayuscula)

# Espacios
txt='   Me deje algunos espacios   '
textoimportante= "clave "

txtcorregido=txt.strip()
txtcorregido2=textoimportante.strip()

print(txtcorregido)
print(txtcorregido2)

# Concatenado
a= 'hola'
b= 'mundo'
c= a + b
d= a + ' ' + b
print(c)
print(d)

txt = 'este curso dura: '
horas= 10
concatenado= txt + str(horas) + ' horas'

print(concatenado)

# Insertar en llaves {}
txt = 'este curso dura: {} horas'
horas= 10

print(txt.format(horas))

txt = 'este curso dura: {} horas y {} clases'
clases=60
horas= 10

print(txt.format(horas,clases))

txt = 'este curso dura: {1} clases y {0} horas'
clases=60
horas= 10

print(txt.format(horas,clases))

# Comillas en comillas

txt= 'la mejor serie que vi es "STAND DE BESOS"' #una forma es poner las comillas inversas que utilizo en la string
txt2= "la mejor serie que vi es \"STAND DE BESOS\"" #si tengo que usar las mismas comillas debo poner las comillas posterior a una barra invertida conocido como "escape de caracteres"

print(txt)
print(txt2)

# Barra en barra

txt3= 'la información esta en c:\CURSO\DIGITAL' #esto me anucia un warning en la sintaxis
txt4= 'la información esta en c:\\CURSO\\DIGITAL' #esta sería la maera correcta de escribirlo

print(txt3)
print(txt4)

# Salto de línea

txt5= 'la mejor serie que vi es: \nSTAND DE BESOS'

print(txt5)

# Tabulado

txt6= 'la mejor serie que vi es: \tSTAND DE BESOS'

print(txt6)

# Borrar un caracter (backspace)

txt7= 'la mejor serie que vi es:\bSTAND DE BESOS'

print(txt7)

# Metodos de String

# Colocar mayúscula

txt8= 'tengo hambre pidemos mc'

print(txt8.capitalize()) #para colocar la primera letra de la oración en mayúscula
print(txt8.title()) #para colocar la primera letra de cada palabra de la oración en mayúscula

# Centrar palabra dentro de x caracteres

txt9= 'lomito'

print(txt9.center(20))

# Contar las veces que aparece un valor en una cadena

txt10= 'son las cinco menos cinco faltan cinco para las cinco cuantas veces dije cinco sin contar el último cinco'

print(txt10.count('cinco'))

# Validar la terminación devuelve booleano

print(txt10.endswith('cinco')) #una forma es buscar por palabra o cadena TRUE
print(txt10.endswith('o')) #otra forma es que puedo buscar por un letra TRUE
print(txt10.endswith('a')) #FALSE

# Buscar la posición

print(txt10.find('menos')) #devuelve la posición donde comienza la palabra
print(txt10.find('cinco')) #devuelve la posición donde comienza la primer palabra igual que encuentra

# Validar si es número

numeros= '12345'
numeros2= '12345abc'
numeros3= '123.5'

print(numeros.isdigit())
print(numeros2.isdigit())
print(numeros3.isdecimal())

# Validar si todo esta en minúscula

print(txt10.islower())

# Validar si todo esta en mayúscula

print(txt10.isupper())