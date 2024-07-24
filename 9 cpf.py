def verificar_cpf(cpf):
    # Remover caracteres que não são dígitos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Calcular o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verif_1 = 0
    else:
        digito_verif_1 = 11 - resto
    
    # Verificar primeiro dígito verificador
    if digito_verif_1 != int(cpf[9]):
        return False
    
    # Calcular o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        digito_verif_2 = 0
    else:
        digito_verif_2 = 11 - resto
    
    # Verificar segundo dígito verificador
    if digito_verif_2 != int(cpf[10]):
        return False
    
    # Se passou por todas as verificações, CPF é válido
    return True

# Função para formatar o CPF com pontos e traço
def formatar_cpf(cpf):
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

# Programa principal
if __name__ == '__main__':
    cpf = input("Digite o CPF (apenas números): ").strip()
    
    if verificar_cpf(cpf):
        print(f"O CPF {formatar_cpf(cpf)} é válido.")
    else:
        print(f"O CPF {formatar_cpf(cpf)} é inválido.")
