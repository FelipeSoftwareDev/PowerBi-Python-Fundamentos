# Estruturas de controle:

# Se queremos controlar quando uma linha de código será executada ou não, usamos o if, por exemplo

idade, nome = (13, "Felipe")

# variáveis e funções com mais de um nome devem ser declaradas com "_", conhecido como snake case

def verificar_idade(idade):
    maioridade = False
    if idade > 18:
        maioridade = True
    return maioridade
   
def resposta(nome, idade, maioridade):
    if maioridade == True:
        print(f'Parabéns {nome} você já pode ser preso!')

    else: 
        print(f'Nossa {nome} só faltam {18 - idade} anos pra você virar um adulto!')
        return