def encontrar_primos(limite):
    # Inicializar uma lista para marcar os números compostos
    marcados = [False] * (limite + 1)
    # Inicializar uma lista para armazenar os números primos
    primos = []
    
    # O Crivo de Eratóstenes
    for numero in range(2, limite + 1):
        if not marcados[numero]:
            # Se o número não está marcado, é primo
            primos.append(numero)
            # Marcar os múltiplos do número como compostos
            for multiplo in range(numero * numero, limite + 1, numero):
                marcados[multiplo] = True
    
    return primos

# Programa principal
if __name__ == '__main__':
    try:
        # Ler o número limite fornecido pelo usuário
        limite = int(input("Digite um número inteiro para encontrar os números primos até ele: "))
        
        # Verificar se o limite fornecido é válido
        if limite < 2:
            print("Por favor, digite um número inteiro maior ou igual a 2.")
        else:
            # Chamar a função para encontrar os números primos até o limite
            primos = encontrar_primos(limite)
            
            # Exibir os números primos encontrados
            print(f"Números primos até {limite}:")
            print(primos)
    
    except ValueError:
        print("Erro: por favor, digite um número inteiro válido.")
