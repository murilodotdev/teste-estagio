def procurar(letra: str, string: str) -> dict:
    """
    Procura uma determinada letra em uma string.
    """

    STRING = string
    LETRA_PROCURADA = letra

    resultado = {
        'ocorrências': 0,
        'vezes em maiúscula': 0,
        'vezes em minúscula': 0
    }

    for i in STRING:
        if i == LETRA_PROCURADA.upper():
            resultado['ocorrências'] += 1
            resultado['vezes em maiúscula'] += 1
        
        if i == LETRA_PROCURADA.lower():
            resultado['ocorrências'] += 1
            resultado['vezes em minúscula'] += 1

    return resultado

while True:
    letra = input('Qual letra procurar?\n')
    string = input('Em qual string?\n')

    print(procurar(letra, string))