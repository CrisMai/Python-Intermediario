
# Escopo local:

def minha_funcao():
    x = 10  # x é uma variável de escopo local
    print(x)

minha_funcao()
# print(x) Isso causaria um erro, pois x não é acessível fora da função.


# Escopo global:

y = 20  # y é uma variável global

def outra_funcao():
    print(y)  # y pode ser acessado aqui

outra_funcao()


# Outro exemplo do uso de global:

contador = 0  # Variável global

def incrementar():
    global contador
    contador += 1  # Modifica a variável global
    print(contador)

incrementar()  # Saída: 1
incrementar()  # Saída: 2