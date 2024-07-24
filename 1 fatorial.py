def fibonacci_sequence(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def is_odd(num):
    return num % 2 != 0

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

# Gerar os 10 primeiros números da sequência de Fibonacci
fibonacci_numbers = fibonacci_sequence(10)

# Encontrar os números ímpares e calcular seus fatoriais
odd_fibonacci_numbers = [num for num in fibonacci_numbers if is_odd(num)]
results = {num: factorial(num) for num in odd_fibonacci_numbers}

# Imprimir os resultados
for num, fact in results.items():
    print(f'O fatorial de {num} é {fact}')
