#programa que mostra os somatório dos números pares de 1 até 500 com for
for i in range (1, 501):
    if i%2==0:
        somatorio=0
        for j in range (1, i+1):
            somatorio+=j
        print("O somatório do número: ",i, "é: ", somatorio)
print("Fim do programa!")