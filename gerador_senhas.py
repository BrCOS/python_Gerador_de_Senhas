import random
print('Gerador de Senhas - By BrCOS')

#Variável senha (vazia)
senha = ''

#Listas
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q' ,'R', 'S', 'T', 'U', 'V', 'W', 'X' ,'Y', 'Z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Entrada de dados
qtd_letras = int(input('Digite a quantidade de letras que deseja em sua senha: \n'))
qtd_numeros = int(input('Digite a quantidade de números que deseja em sua senha: \n'))
qtd_especiais = int(input('Digite a quantidade de caracteres especiais que deseja em sua senha: \n'))

ordem_senha = int(input('''Como você quer a sua senha?
\n Digite 1 para que a senha seja ordenada.
\n Digite 2 para que a senha seja randomizada.
\n Digite o número correspondente: '''))

#Loop For
for i in range(qtd_letras):
    senha = senha + random.choice(letras)

for i in range(qtd_numeros):
    senha = senha + random.choice(numeros)

for i in range(qtd_especiais):
    senha = senha + random.choice(simbolos)

#Condicional
if ordem_senha == 1:
    print(f'''Senha Gerada com sucesso!
    Sua senha é: {senha}''')

elif ordem_senha == 2:
    #random.shuffle não pode ser usado em string só em listas!
    senha = list(senha)#convertendo senha para lista
    random.shuffle(senha)#embaralhando a senha
    senha = "".join(senha)#método .join converte uma lista str em str e uma string vazia é adicionada entre os elementos da lista.
    print(f'''Sua senha foi gerada com sucesso!
    Sua senha é: {senha}''')

else:
    print('Você digitou um número inválido, digite 1 ou 2.')