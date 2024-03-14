while True:
    n = int(input("digite um número inteiro: "))
    fatorial=1
    for i  in range(1, n+1):
        fatorial = fatorial * i
    print(fatorial)
    continuar = input("Deseja continuar? (s/n): ")
    if continuar == "n":
        break