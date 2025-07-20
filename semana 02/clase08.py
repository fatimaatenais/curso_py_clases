"""
crear 4 variables entre enteros, floats, booleans, string
realizar el uso de condicionales de las variables para dos casos true y 2 casos false
en casos de true imprimir el valor de de las otras dos variables
en dos condicionales compararlo con un numero (>, <)

"""
# 1er requisito
nombre1 = "Atenaís"
edad1 = 17
altura1 = 1.58
estudiante1 = True

nombre2 = "Luana"
edad2 = 19
altura2 = 1.60
estudiante2 = False

# 2do requisito
if estudiante1:
    print("Hola soy {}, tengo {}, mido {}".format(nombre1, edad1, altura1))
if estudiante2:
    print("Hola soy {}, tengo {}, mido{}".format(nombre2, edad2, altura2))

if altura2 > altura1:
    print("{} es menor que {}".format(nombre1, nombre2))
if altura2 < altura1:
    print("{} es mayor que {}".format(nombre1, nombre2))


