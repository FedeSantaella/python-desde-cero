

from ast import Break
import random


numero_secreto = random.randint (0,100)
adivinado= False
cantidad_intentos=0
cant_max_intentos= 5

"""print(adivinado)
bucle=not adivinado
print(bucle)
print(adivinado)""" #explicación de la función de while not adivinado. While necesita una afirmación para que podamos ingresar al bucle si leyera false no ingresa directamente.

print("¡Bienvenido al juego de adivinar el número secreto")

"""while not adivinado and cantidad_intentos < cant_max_intentos:
    numero = int(input("introduce un número del 1 al 99: ")) 

    if numero == numero_secreto:
        print("¡Felicitaciones has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("el número es mayor al ingresado")
    else:
        print("el número es menor al ingresado")
    cantidad_intentos += 1

if not cantidad_intentos < cant_max_intentos:
    print ("Game over!")""" # PRIMERA OPCION sin break

while not adivinado and cantidad_intentos < cant_max_intentos:
    if not cantidad_intentos < cant_max_intentos:
        print ("Game over!")
        break

    numero = int(input("introduce un número del 1 al 99: ")) 

    if numero == numero_secreto:
        print("¡Felicitaciones has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("el número es mayor al ingresado")
    else:
        print("el número es menor al ingresado")
    cantidad_intentos += 1
    
# --------------------------- SUBIR A GIT HUB
#solo por esta vez debemos hacer esto para vincular con nuestro git hub configurar nuestro nombre y mail(igual al de la plataforma)
#VIEW/TERMINAL/PS C:\Users\fede_\OneDrive\Desktop\Cursos\Python Desde Cero> git config --global user.name 
#luego de configurar el user debo configurar el mail C:\Users\fede_\OneDrive\Desktop\Cursos\Python Desde Cero> git config --global user.email