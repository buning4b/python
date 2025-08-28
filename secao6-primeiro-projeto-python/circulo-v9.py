from math import pi

# Retorna um valor


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input("Raio do seu circulo: ")
    circulo(raio)
    area = circulo(raio)
    print (f"Área do circulo: {area}")
