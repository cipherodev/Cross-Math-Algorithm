"""
cipherodev 2025
"""
from random import randint

def cross_math_sol():
    a = randint(1, 9)
    b = randint(1, 9)
    c = randint(1, 9)
    d = randint(1, 9)
    e = randint(1, 9)
    f = randint(1, 9)
    g = randint(1, 9)
    h = randint(1, 9)
    i = randint(1, 9)

    result = a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10
    equation = f"{a} + 13 * {b} / {c} + {d} + 12 * {e} - {f} - 11 + {g} * {h} / {i} - 10"

    return result, equation

while True:
    guess, eq = cross_math_sol()
    if guess == 66:
        print(f"SOLVED WITH THE ANSWER OF: {guess}\nEQUATION: {eq}")
        break
    else:
        print(f"INCORRECT ANSWER: {guess} | Equation: {eq}")