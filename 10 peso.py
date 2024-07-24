def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc <= 24.9:
        return "Peso ideal (parabéns)"
    elif imc >= 25.0 and imc <= 29.9:
        return "Levemente acima do peso"
    elif imc >= 30.0 and imc <= 34.9:
        return "Obesidade grau I"
    elif imc >= 35.0 and imc <= 39.9:
        return "Obesidade grau II (severa)"
    else:
        return "Obesidade grau III (mórbida)"

# Programa principal
if __name__ == '__main__':
    try:
        peso = float(input("Digite o peso da pessoa (em kg): "))
        altura = float(input("Digite a altura da pessoa (em metros): "))
        
        imc = calcular_imc(peso, altura)
        condicao_imc = classificar_imc(imc)
        
        print(f"O IMC calculado é: {imc:.2f}")
        print(f"Condição de acordo com o IMC: {condicao_imc}")
        
    except ValueError:
        print("Erro: por favor, digite um valor numérico válido para peso e altura.")
