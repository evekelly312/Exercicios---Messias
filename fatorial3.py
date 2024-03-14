resp="sim"
while resp=="sim":
    n=int(input("Digite um número"))
    fatorial=1
    for i in range(1,n+1):
        fatorial=fatorial*i
    print("O fatorial de",n,"é",fatorial)
    resp=input("Deeja calcular o fatorial de outro número? (sim/não)")