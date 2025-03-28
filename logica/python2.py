# Estruturas de controle:

# Se queremos controlar quando uma linha de código será executada ou não, usamos o if, por exemplo

idade, nome = (25, "Felipe")

def verificar(idade):
    maioridade = False
    if idade > 18:
        maioridade = True
    return maioridade
   
def resposta(nome, idade, maioridade):
    if maioridade == True:
        print(f'Parabéns {nome} você já pode ser preso!')

    else: 
        print(f'E aí {nome} essa escola termina quando?')
        return