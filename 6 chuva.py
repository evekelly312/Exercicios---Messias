# Número de dias em junho (considerando 30 dias)
num_dias_junho = 30

# Lista para armazenar os índices pluviométricos de cada dia
indices_pluviometricos = []

# Leitura dos índices pluviométricos de cada dia do mês
for dia in range(1, num_dias_junho + 1):
    indice = float(input(f"Digite o índice pluviométrico para o dia {dia}: "))
    indices_pluviometricos.append(indice)

# Encontrar o dia que mais choveu e o dia que menos choveu
dia_mais_chuvoso = 1
dia_menos_chuvoso = 1
max_chuva = indices_pluviometricos[0]
min_chuva = indices_pluviometricos[0]

for dia in range(1, num_dias_junho):
    if indices_pluviometricos[dia] > max_chuva:
        max_chuva = indices_pluviometricos[dia]
        dia_mais_chuvoso = dia + 1
    if indices_pluviometricos[dia] < min_chuva:
        min_chuva = indices_pluviometricos[dia]
        dia_menos_chuvoso = dia + 1

# Calcular médias pluviométricas das duas quinzenas
media_primeira_quinzena = sum(indices_pluviometricos[0:15]) / 15
media_segunda_quinzena = sum(indices_pluviometricos[15:num_dias_junho]) / (num_dias_junho - 15)

# Imprimir resultados
print(f"O dia que mais choveu foi o dia {dia_mais_chuvoso} com {max_chuva} mm.")
print(f"O dia que menos choveu foi o dia {dia_menos_chuvoso} com {min_chuva} mm.")
print(f"Média pluviométrica da primeira quinzena: {media_primeira_quinzena:.2f} mm")
print(f"Média pluviométrica da segunda quinzena: {media_segunda_quinzena:.2f} mm")
