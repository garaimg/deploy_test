import math


def es_primo(n):
    if n < 0:
        return 'No es posible devolver números primos.'

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # La razón por la cual el bucle comienza desde 2 y va hasta la raíz cuadrada de n es porque no es necesario verificar más allá de la raíz
    # cuadrada para determinar si un número es primo. Si un número es divisible por un número mayor que su raíz cuadrada, entonces también
    # será divisible por un número menor que su raíz cuadrada.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplica(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return 'No se puede dividir por cero.'
    return a / b
