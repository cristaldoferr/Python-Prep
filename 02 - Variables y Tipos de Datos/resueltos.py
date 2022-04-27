# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

num = 25
print(num)

# 2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1

print(type(num))

# 4) Crear una variable que contenga tu nombre

my_name = "Ezequiel"

# 5) Crear una variable que contenga un número complejo

num_complejo = 5 + 5j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5

print(type(num_complejo))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

num_pi = 3.1416

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

one_true = "True" # - Esto es un string
two_true = True # - Esto es un valor booleano
"""
No tienen nada que ver uno del otro. No son lo mismo.
"""

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

print(type(one_true))
print(type(two_true))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

sum = 25 + 17.5

# 11) Realizar una operación de suma de números complejos

a = 3 + 3j
b = 4 + 4j

print(a + b)

# 12) Realizar una operación de suma de un número real y otro complejo

c = a + 25.4
print(c)

# 13) Realizar una operación de multiplicación

print(7 * 5)

# 14) Mostrar el resultado de elevar 2 a la octava potencia

print(2**8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

cociente = 27 / 4
print(cociente)

# 16) De la división anterior solamente mostrar la parte entera

27 // 4

# 17) De la división de 27 entre 4 mostrar solamente el resto

27 % 4

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

6 * 4 + 3

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

opt_one = "Fernando"
opt_two = "Cristaldo"

print(opt_one + opt_two)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

print("2" == 2)

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

three = 3
three -= 1
print(three)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

1 << 2

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

2 + '2'
# No esta permitido sumar un tipo string con un tipo int
# Si los dos fueran de tipo string, se concatenaria y daría como resultado 22

# 26) Realizar una operación válida entre valores de tipo entero y string

int_one = 2
str_one = '2'

print(int_one + int(str_one))