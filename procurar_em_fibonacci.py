from time import sleep
from os import system

def fibonacci(n: int) -> None:
    """
    Procura um determinado na sequência de fibonacci e retorna uma mensagem dizendo se pertence ou não a sequência.

    Paramêtros:
        n: Número a ser procurado.
    """
    sequencia = [0, 1]

    while True:
        z = sequencia[-1] + sequencia[-2]

        try:
            system('cls')
        except:
            pass

        print(f'Procurando...\n{z}')
        sleep(0.03) # <-- Tempo entre cada atualização de tela

        sequencia.append(z)
        if z == n:
            return f'O número {n} pertence a sequência!'
        if z > n:
            return f'O número {n} não pertence a sequência.'

while True:  
    numero = int(input("Digite um número inteiro.\n"))

    print(fibonacci(numero))