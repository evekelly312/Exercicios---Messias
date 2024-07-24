def cifra_de_cesar(mensagem):
    chave = 3
    mensagem_criptografada = ""
    
    for char in mensagem:
        # Verifica se o caractere é uma letra minúscula
        if char.islower():
            # Encripta o caractere e adiciona ao resultado
            mensagem_criptografada += chr((ord(char) - ord('a') + chave) % 26 + ord('a'))
        # Verifica se o caractere é uma letra maiúscula
        elif char.isupper():
            # Encripta o caractere e adiciona ao resultado
            mensagem_criptografada += chr((ord(char) - ord('A') + chave) % 26 + ord('A'))
        else:
            # Se não for letra, mantém o caractere original
            mensagem_criptografada += char
    
    return mensagem_criptografada

# Recebe a mensagem do usuário
mensagem = input("Digite a mensagem que deseja criptografar: ")

# Chama a função para criptografar a mensagem
mensagem_criptografada = cifra_de_cesar(mensagem)

# Imprime a mensagem criptografada
print("Mensagem criptografada:", mensagem_criptografada)
