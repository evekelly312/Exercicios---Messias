def calcular_preco_aluguel(km_percorridos, dias_alugados):
    preco_diaria = 90  
    preco_km = 0.20    
    
    # Calcular o valor total do aluguel
    valor_diarias = dias_alugados * preco_diaria
    valor_km = km_percorridos * preco_km
    preco_total = valor_diarias + valor_km
    
    return preco_total

# Programa principal
if __name__ == '__main__':
    try:
        km = float(input("Digite a quantidade de quilômetros percorridos: "))
        dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
        
        preco_total = calcular_preco_aluguel(km, dias)
        
        print(f"O preço total a pagar pelo aluguel do carro é: R${preco_total:.2f}")
    
    except ValueError:
        print("Erro: por favor, digite valores numéricos válidos para os quilômetros e dias.")
