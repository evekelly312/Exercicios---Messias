import math

def calcular_area_circunferencia(raio):
    area = math.pi * raio**2
    return area

def main():
    try:
        raio = float(input("Digite o raio da circunferência: "))
        if raio < 0:
            print("O raio não pode ser negativo.")
        else:
            area = calcular_area_circunferencia(raio)
            print(f"A área da circunferência com raio {raio} é {area:.2f} unidades quadradas.")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número.")

if __name__ == "__main__":
    main()
