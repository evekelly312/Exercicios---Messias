populacao_a = 5000000 
taxa_a = 0.03 
populacao_b = 7000000 
taxa_b = 0.02  

anos = 0

while populacao_a <= populacao_b:
    anos += 1
    populacao_a *= (1 + taxa_a)  
    populacao_b *= (1 + taxa_b)  

# Imprime o tempo necessário para que a população do país A ultrapasse a população do país B
print(f"Serão necessários {anos} anos para a população do país A ultrapassar a população do país B.")
