la = int(input("Digite o comprimento do lado a em centímetros: "))
lb = int(input("Digite o comprimento do lado b em centímetros: "))
lc = int(input("Digite o comprimento do lado c em centímetros: "))

if la == lb == lc:
   print("É umngulo equilátero.")

elif la == lb or lb == lc or lc == la:
   print("É um triângulo isósceles.")

else:
   print("É um triângulo escaleno.")

if la + lb > lc and la + lc > lb and lb + lc > la:
   print("Os comprimentos dos lados formam um triângulo válido.")
else:
   print("Os comprimentos dos lados não formam um triângulo válido.")
