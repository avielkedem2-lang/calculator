def power(base, exponent):

    return base ** exponent

def square_root(n):

    if n < 0:
        return "there is no root for a negative number!"
    return n ** 0.5
def modulo(a, b):
    return a % b


def factorial(n):
    if n < 0:
        return "error: you can't put negative number!"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result