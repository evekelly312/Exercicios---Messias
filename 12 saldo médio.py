def calcular_credito(saldo_medio):
    if saldo_medio <= 200:
        return 0  # nenhum crédito
    elif saldo_medio <= 400:
        return 0.2 * saldo_medio  # 20% do saldo médio
    elif saldo_medio <= 600:
        return 0.3 * saldo_medio  # 30% do saldo médio
    else:
        return 0.4 * saldo_medio  # 40% do saldo médio

# Programa principal
if __name__ == '__main__':
    try:
        saldo_medio = float(input("Digite o saldo médio do cliente: "))
        
        credito = calcular_credito(saldo_medio)
        
        print(f"Saldo médio: R${saldo_medio:.2f}")
        print(f"Valor do crédito especial: R${credito:.2f}")
    
    except ValueError:
        print("Erro: por favor, digite um valor numérico para o saldo médio.")
