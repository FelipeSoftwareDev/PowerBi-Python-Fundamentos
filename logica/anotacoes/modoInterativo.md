O modo Interativo permite que você veja o resultado enquanto desenvolve o código, sem ter que ficar colocando o código pra rodar.

Perceba porém que esse modo vai acessar diretamente o terminal, então não é algo recomendado para projetos reais, serve basicamente para fazer testes rápidos, verificar como os operadores se comportam em determinadas funções, etc. Em geral testar algo simples de forma mais rápida.

pode ser iniciado chamando apenas o interpretador (python) ou executando o script com flag -i(python -i app.py), se for fazer da primeira forma faremos no próprio terminal do vs code ou ainda no terminal do windows/linux/mac os 



# Função dir: retorna a lista de nomes que existam no escopo local atual, no escopo em que ela foi chamada. Se eu passar ele com um argumento (entre parenteses, algo como parametros
# de uma função), ele retornará uma lista de atributos válidos para o objeto! 

# ESTÃO AQUI APENAS A CARÁTER DE EXEMPLO, ESSA FUNÇÃO É USADA NO MODO INTERATIVO!!! USADA APENAS PARA MANTER MELHOR CONTROLE DAS VARIÁVEIS E TER UMA IDÉIA DO QUE PODE SER FEITO
# COM O QUE VOCÊ JÁ TEM

dir()

dir(100)

# Outra forma legal de ter essa documentação e literalmente ver as dicas de como funcionam na prática é também no modo interativo digitar help(variável), por exemplo:

help(100)