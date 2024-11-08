

# Retorno de um valor simples:

def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)  # Saída: 8


# Retorno de múltiplos valores:

def calcular(a, b):
    soma = a + b
    produto = a * b
    return soma, produto

soma, produto = calcular(2, 4)
print(soma)     # Saída: 6
print(produto)  # Saída: 8


# Outro exemplo de retorno de funções

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y

# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))