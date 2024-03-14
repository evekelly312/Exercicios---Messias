#tabuada de multiplifação de um numero qualquer om while
while True:
    n =  int(input("Digite um numero para ver a tabuada: "))
    i = 1
    while i <= 10:
        print(n, "x", i, "=", n*i)
        i += 1
    continua=input("Deseja continuar? (sim/não)")
    if continua=="nao":
        break
        