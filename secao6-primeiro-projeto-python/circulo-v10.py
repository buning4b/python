from math import pi
import sys
# Retorna um valor


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = sys.argv[1]
    circulo(raio)
    area = circulo(raio)
    print (f"Área do circulo: {area}")  
