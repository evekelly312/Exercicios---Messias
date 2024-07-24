def calcular_imposto(salario):
    if salario <= 1500.00:
        imposto = salario * 0.05
    elif salario <= 3000.00:
        imposto = salario * 0.08
    elif salario <= 10000.00:
        imposto = salario * 0.15
    else:
        imposto = salario * 0.27
    
    return imposto

# Função para imprimir os resultados
def imprimir_resultados(salario, imposto, salario_liquido):
    print(f"Salário Bruto: R$ {salario:.2f}")
    print(f"Imposto de Renda Devido: R$ {imposto:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Programa principal
while True:
    # Solicitar o salário do funcionário
    salario = float(input("Digite o salário do funcionário (ou digite 0 para encerrar): R$ "))
    
    if salario == 0:
        break
    
    # Calcular o imposto de renda devido
    imposto_devido = calcular_imposto(salario)
    
    # Calcular o salário líquido
    salario_liquido = salario - imposto_devido
    
    # Imprimir os resultados
    imprimir_resultados(salario, imposto_devido, salario_liquido)
    
    # Espaçamento entre execuções
    print("\n")

print("Programa encerrado.")
