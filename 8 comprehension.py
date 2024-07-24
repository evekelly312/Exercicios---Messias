# Definindo o tamanho da matriz
n = 4 

# Criando a matriz usando List Comprehension
matriz = [[i * n + j + 1 for j in range(n)] for i in range(n)]

# Imprimindo a matriz
print("Matriz:")
for linha in matriz:
    print(linha)

# Imprimindo a diagonal principal da matriz
print("\nDiagonal principal:")
diagonal_principal = [matriz[i][i] for i in range(n)]
print(diagonal_principal)
