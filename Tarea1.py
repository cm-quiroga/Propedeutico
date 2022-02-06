sum = 1 + 2 # 3
x = sum * 2
print(x)

# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
print(type(distancia_a_alfa_centauri))

# Importamos la biblioteca
from cgi import print_directory
from datetime import date

# Mostramos la fecha en la consola
print(date.today())

# Para transformar el tipo de datos se coloca str() tambien puede ser float()
print("La fecha de hoy es: " + str(date.today()))


# Llamar unavariable que contiene un string ""
print("Bienvenido al programa")
name = input("Introduzca su nombre: ")
print("Bienvenido " + name)


# Pasar de str a float para obtener una operacion matematica. Por defecto input es string
print("Calcular")
Primer_numero = float(input("first number: "))
Segundo_numero = float(input("second number: "))
print(Primer_numero + Segundo_numero)



print("Calcular")
Primer_numero = float(input("first number: "))
Segundo_numero = float(input("second number: "))
print(int(Primer_numero) + int(Segundo_numero))