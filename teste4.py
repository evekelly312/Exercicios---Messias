def calcular_salario_liquido(valor_hora_aula, horas_trabalhadas, percentual_inss):
    salario_bruto = valor_hora_aula * horas_trabalhadas
    desconto_inss = (salario_bruto * percentual_inss) / 100
    salario_liquido = salario_bruto - desconto_inss
    return salario_liquido

def main():
    try:
        valor_hora_aula = float(input("Digite o valor da hora-aula: "))
        horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
        percentual_inss = float(input("Digite o percentual de desconto do INSS: "))

        salario_liquido = calcular_salario_liquido(valor_hora_aula, horas_trabalhadas, percentual_inss)

        print(f"Salário Líquido: R$ {salario_liquido:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")

if __name__ == "__main__":
    main()
