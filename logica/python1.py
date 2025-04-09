# Aonde usaremos Python? Olha, é mais fácil dizer aonde não usaremos!
# só não usaremos Python em aplicativos de celular/mobile, de resto ele é bem versátil
# É uma linguagem multiplataforma e multiparadigma.





# a função nativa: print, como o nome já diz, imprime algo no terminal.
# Vamos escrever nossa mensagem entre aspas duplas ou simples, apenas para que o computador entenda isso como um texto.

print ('olá mundo')

# linguagem de tipagem forte e dinâmica
# dinamica porque não preciso necessariamente falar qual o tipo daquela variável, por exemplo que um número é um int (inteiro), embora eu possa fazê-lo até para converter em
# outro tipo

print (5 + 10)

#Perceba que só de n ter pontos e não estar entre aspas o próprio Python já "tipa" como int

#Tipagem forte não me permite por exemplo realizar contas usando número e letras, exemplo "a" - int(18), vai dar erro.
# Embora haja o problema de lógica de acabar concatenando números ou número e letras, exemplo tendo números definidos como string (""), ao somarmos resultam em concatenação
# nesse exemplo os dois foram definidos propositalmente como string para mostrá-los o resultado que será gerado 

print('22' + '55')

# Já se um dos dois estivesse como int (número inteiro) ou float (número quebrado/com vírgula) e o outro como string(texto), o retorno seria erro, não permitindo a operação
# e ainda nos avisando que strings podem apenas ser concatenadas!!!




# para entender melhor o tipo booleano (v ou f) vamos declara que variáveis têm o valor v ou f. Para isso basta colocar o nome da variável, um "=" que nesse caso é a atribuição
# de valor e depois o seu valor.

a = True
b = False

print(a, b)

# por último vamos criar uma função usando um pouco do que aprendemos 
# Para deifinir uma função usaremos o a palavra reservada "def", depois o nome que queremos dar à função, (os parametros entre aspas), ":" e por fim, a função em baixo com
# indentação obrigatória

c = "22"
d = "13"

def concat():
    return c + d

print(concat())

# O Python vai tipar por debaixo dos panos os dados, podemos porém converter eles da forma
# tradicional para ter certeza que o dado estará na tipagem correta quando usado (pelo menos nesse momento)

int()
float()
bool()
str()
# exemplo
e = float(10)
f = float(11.5)

print(e, f, e + f)

# No Python, podemos declarar variáveis na mesma linha apenas separando-as por vírgula:

idade, nome = (25, 'Felipe')

print(f'Me chamo {nome} e tenho {idade} anos!')

# Detalhe MUITO IMPORTANTE!!! NÃO HÁ constantes em Python, usamos de convenção para avisar que uma variável não pode ser mechida
# ,tal qual uma constante, o nome todo em maiúsculo. Isso avisará aos outros programadores que não devem alterar o valor da mesma, exemplo:

CONSTANTE = True
