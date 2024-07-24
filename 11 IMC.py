def verificar_classificacao(notas):
    if all(nota >= 7.0 for nota in notas):
        return 'A - Passou em todos os exames'
    elif notas[0] >= 7.0 and notas[1] >= 7.0 and notas[3] >= 7.0 and (notas[2] < 7.0 or notas[4] < 7.0):
        return 'B - Passou em I, II e IV, mas não em III ou V'
    elif notas[0] >= 7.0 and notas[1] >= 7.0 and (notas[2] >= 7.0 or notas[3] >= 7.0) and notas[4] < 7.0:
        return 'C - Passou em I e II, III ou IV, mas não em V'
    else:
        return 'Reprovado - Outras situações'

# Programa principal
if __name__ == '__main__':
    try:
        notas = []
        for i in range(5):
            nota = float(input(f"Digite a nota do exame {i+1}: "))
            notas.append(nota)
        
        classificacao = verificar_classificacao(notas)
        
        print(f"Classificação do aluno: {classificacao}")
    
    except ValueError:
        print("Erro: por favor, digite notas válidas (números).")
