# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# num = 12

# if num > 0:
#    print('Mayor que cero')
# elif num < 0:
#    print('Menor que cero')
# else:
#    print('Igual a cero')

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# a = 8
# b = 'hola'

# if a == b:
    # print('Mismo tipo')
# else:
    # print('Distinto tipo')

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# for n in range(1, 20+1):
    # if n % 2 == 0:
        # print(n)

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# for x in range(0, 5+1):
    # print(f'El resultado de elever {x} a la maxima potencia de 3 es: {x**3}')

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# a = 16

# for n in range(1, a+1):
    # print(n)

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

num = 12

# 7) Crear un ciclo for dentro de un ciclo while

i = 1

while (i < 10):
    for x in range(i, 10+1):
        print(i)
        i = i + x
        if i == 29:
            break

# 8) Crear un ciclo while dentro de un ciclo for

# 9) Imprimir los números primos existentes entre 0 y 30

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6