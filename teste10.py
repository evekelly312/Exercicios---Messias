n1 =float(input("Primeira nota: "))
n2 =float(input("Segunda nota: "))
n3 =float(input("Terceira nota: "))
n4 =float(input("Quarta nota: "))

media = (n1+n2+n3+n4) / 4
if media >= 7:
    print("Aprovado com média:", media)
else:
    print("Reprovado com media: ", media)

