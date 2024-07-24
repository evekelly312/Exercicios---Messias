# Função para calcular a moda de uma lista
def calcular_moda(lista):
    
    contagem = {}
    for elemento in lista:
        if elemento in contagem:
            contagem[elemento] += 1
        else:
            contagem[elemento] = 1
    
    moda = None
    max_contagem = 0
    for elemento, freq in contagem.items():
        if freq > max_contagem:
            moda = elemento
            max_contagem = freq
    
    return moda

# Função para calcular a mediana de uma lista
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)
    if tamanho % 2 == 1:
       
        mediana = lista_ordenada[tamanho // 2]
    else:
       
        mediana = (lista_ordenada[tamanho // 2 - 1] + lista_ordenada[tamanho // 2]) / 2
    
    return mediana

# Função para calcular a média de uma lista
def calcular_media(lista):
    return sum(lista) / len(lista)


lista_inteiros = []
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    lista_inteiros.append(numero)


moda = calcular_moda(lista_inteiros)
mediana = calcular_mediana(lista_inteiros)
media = calcular_media(lista_inteiros)

print(f"A moda dos elementos na lista é: {moda}")
print(f"A mediana dos elementos na lista é: {mediana}")
print(f"A média dos elementos na lista é: {media}")
