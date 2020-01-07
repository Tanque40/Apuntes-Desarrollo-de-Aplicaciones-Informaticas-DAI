################### Funciones #########################

# Para ocupar reduce se importa del módulo functools
from functools import reduce

# Una función sin parámetros y que solo muestra un mensaje
def holaMundo():
    print("Hola Mundo desde una Función!")

# Una función que ocupa un solo parámetro y lo eleva al cuadrado
# Tiene como parámetro:
#   n = el valor a elevar al cuadrado
def elevarAlCuadrado(n):
    return n ** 2

# Una funcion que devuelve la suma de 2 números
# Tiene como parámetros:
#   a = el primer número de la suma
#   b = el segundo número de la suma
# Se ocupa la palabra reservada return para regresar la suma
def suma(a, b):
    return a + b

# Una función que devuelve la división y el residuo de la misma
# Tiene como parámetros:
#   x = diviendo
#   y = divisor
def divisionResiduo(x, y):
    division = x / y
    residuo = x % y
    return division, residuo

# Una funcion que devuelve una lista con números elevados al cuadrados ocupando la función map
# Tenemos como parámetros:
#   numeros = una lista con n cantidad de números
def elevarListaAlCuadrado(numeros):
    # A cada elemento de numeros se le aplica la función elevarAlCuadrdo
    # y finalmente se transforma en lista lo devuelto por map
    return list(map(elevarAlCuadrado, numeros))

# Una funcion que suma los elementos de 2 listas ocupando la función suma hecha previamente y devuelve los resultados en otra lista
# Tenemos como parámetros:
#   list1 = la lista de números 1
#   list2 = la lista de números 2
def sumaList(list1, list2):
    # A la función map le podemos pasar tantos parámetros como necesitemos
    return list(map(suma, list1, list2))

# Una función que devuelve una lista con los números pares de una lista con el uso de la función lambda
# Tenemos como parámetros:
#   list = la lista a filtrar
# Se ocupará una función lambda para filtrar los datos pares
def obtenerPares(list):
    return list(filter(lambda x: x % 2 == 0, list))

# Una función que obtenga el mayor número de una lista ocupando reduce
# Tenemos como parámetros:
#   list = lista a reducir al mayor
# Se ocupará una función lambda para obtener el mayor de todos
def obtenerMayor(list):
    def f(a, b): return a if (a > b) else b
    return list(reduce(f, list))

################### Funciones Lambda #########################


# Una función lamda que duplica un valor
def duplicar(x): return x * 2

# Una función que eleva a cualquier potencia cualquier valor
def elevar(base, potencia): return base ** potencia

# Una función que devuelve el mayor de dos números
def mayor(a, b): return a if(a > b) else b


################### Ejemplos de Uso #########################

# Función holaMundo()
holaMundo()

print("\n" + ("#" * 32) + "\n")

# Función elevarAlCuadrado(n)
aElevar = 4
print("Número a elevar:" + str(aElevar))
print("Número elevado:" + str(elevarAlCuadrado(aElevar)))

print("\n" + ("#" * 32) + "\n")

# Función suma(a, b)
x = 10
y = 23
print("La suma de " + str(x) + " + " + str(y) + " = " + str(suma(x, y)))

print("\n" + ("#" * 32) + "\n")

# Funcion divisionResiduo(x, y)

dividendo = 50
divisor = 2
resultados = divisionResiduo(dividendo, divisor)
print("La división de " + str(dividendo) + " / " + str(divisor) + " = " + str(resultados[0]))