# Estruturas de controle:

# Se queremos controlar quando uma linha de código será executada ou não, usamos o if, por exemplo

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
    
idade, nome = (13, "Felipe")

maioridade = verificar_idade(idade)
resposta(nome, idade, maioridade)


# Agora vamos fazer uma versão interativa usando o comando de entrada de dados do pyhton

# Função que verifica se a idade é válida e se a pessoa é maior de idade
def verificar_idade_interativo(idade_usuario, nome_usuario):
    if idade_usuario > 0 and idade_usuario < 120:
        return idade_usuario > 18
    else:
        print(f'Por favor, {nome_usuario}, insira sua idade real.')
        return None

# Função que responde com base na idade
def resposta_interativo(maioridade, idade_usuario, nome_usuario):
    if maioridade == True:
        print(f'Bem-vindo {nome_usuario}, você pode entrar na festa. 🎉')
    elif maioridade == False:
        print(f'Perdão {nome_usuario}, volte daqui a {18 - idade_usuario} anos.')
    else:
        print('Não foi possível verificar sua idade.')

# Parte interativa (sem tratamento de erro com try/except)
idade_digitada = input('Insira sua idade: ')
nome_usuario = input('Insira seu nome: ')

# Convertendo a idade para número inteiro
idade_usuario = int(idade_digitada)

# Chamando as funções
maioridade = verificar_idade_interativo(idade_usuario, nome_usuario)
resposta_interativo(maioridade, idade_usuario, nome_usuario)
