from math import pi

# Não retorna, apenas imprimi no console
def circulo(raio):
    print(f"Essa é a área do seu circulo: {pi * float(raio) ** 2:.2f}")


if __name__ == '__main__':
    raio = input("Raio do seu circulo: ")
    circulo(raio)
