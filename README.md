## EXERCÍCIO 1                   
A ampliação do Ensino Fundamental para nove anos de duração, tornou a matrícula da criança obrigatória a partir dos seis anos de idade. Implemente um programa que fornecidos o nome e a idade de uma criança classifique-a em uma das seguintes etapas de ensino:  
 
    Ensino 	                              Faixa etária 
    Educação Infantil	              1 a 5 anos
 	Ensino Fundamental I                  6 a 10 anos
 	Ensino Fundamental II                 11 a 14 anos
  	Ensino Médio                          Maiores de 15 anos
 	 
 
O usuário deve ainda ter a opção de escolher se quer encerrar o programa ou não. 
```
while True: # cria-se um laço de repetição
    try: # tente
        nome = input('Por favor, digite o nome da criança: ') # usuário digita o nome da criança
        while not len(nome): # enquanto tamanho da variável nome for igual a zero o programa continuará a solicitar nome para o usuário
            nome = input('Por favor, digite o nome da criança: ')
        idade = int(input('Por favor, informe a idade da criança (desconsiderar meses): ')) # usuário digita a idade da criança

        if idade >= 1: # cria-se a primeira condição: se idade for maior ou igual 1, se verdadeiro seguirá para as próximas condições
            if idade <= 5: # verifica se idade é menor ou igual a 5, ou seja, 1º faixa etária: 1 a 5 anos
                print('Aluno(a) {}, tem {} anos.\nEstá no Ensino Infantil.\n'.format(nome, idade)) # aparecerá para o usuário esta mensagem
            elif idade >= 6 and idade <= 10: # senão se, verifica se idade está no intervalo da 2º faixa etária: de 6 a 10 anos
                print('Aluno(a) {}, tem {} anos.\nEstá no Ensino Fundamental I.\n'.format(nome, idade)) # aparecerá para o usuário esta mensagem
            elif idade >= 11 and idade <= 14: # senão se, verifica se idade está no intervalo da 3º faixa etária: de 11 a 14 anos
                print('Aluno(a) {}, tem {} anos.\nEstá no Ensino Fundamental II.\n'.format(nome, idade)) # aparecerá para o usuário esta mensagem
            elif idade >= 15: # senão se, verifica se idade é 15 anos ou mais, ou seja, última faixa etária: maiores de 15 anos
                print('Aluno(a) {}, tem {} anos.\nEstá no Ensino Médio.\n'.format(nome, idade)) # aparecerá para o usuário esta mensagem
        else: # senão, caso a primeira condição criada: se idade maior ou igual 1 seja falso:
            print('Idade da criança deve ser a partir de 1 ano.') # esta mensagem aparecerá para o usuário

    except: # caso usuário informe algum dado inválido exemplo: letra ao invés de número na variável idade
        print('Dados inválidos.')
        continue # o programa retorna ao início do laço de repetição

    encerrar = int(input('Deseja encerrar o programa?\nDigite 0 - Sim \nDigite 1 - Não\n')) # usuário informa se deseja encerrar o programa, escolhendo opção 0 - Sim ou 1 - Não

    while encerrar != 0 and encerrar != 1: # cria-se um laço de repetição enquanto o usuário não informar a opção correta:
        print('Opção inválida!') # esta mensagem aparecerá para o usuário
        encerrar = int(input('Deseja encerrar o programa?\nDigite 0 para Sim\nDigite 1 para Não\n')) # laço repete até que a opção escolhida esteja correta

    if encerrar == 0: # se usuário digitou zero, então encerra-se o programa
        print('Programa finalizado com sucesso!') # esta mensagem aparecerá para o usuário
        break # encerra-se laço de repetição
    else: # senão
        continue # o programa retorna ao início do laço de repetição
```
## EXERCÍCIO 2                          
Faça um programa que solicite que o usuário digite um nome. O programa deve imprimir na tela o nome convertido no seguinte formato: 
L*C!@N&  
Para isso, o programa deve ser capaz de converter o nome digitado para maiúsculas e substituir as vogais pelos símbolos apresentados na tabela abaixo.

    A   @ 
    E   &
    I   !
    O   #
    U   *
```
nome = input('Digite um nome: ').upper() # usuário digita um nome, método upper converte o nome digitado para maiúsculo

print(nome) # aparecerá o nome digitado pelo usuário em maiúsculo


nome = nome.replace('A','@') # O método replace procura todas letras 'A' na variável nome e substituí por '@'
nome = nome.replace('E','&') # O método replace procura todas letras 'E' na variável nome e substituí por '&'
nome = nome.replace('I','!') # O método replace procura todas letras 'I' na variável nome e substituí por '!'
nome = nome.replace('O','#') # O método replace procura todas letras 'O' na variável nome e substituí por '#'
nome = nome.replace('U','*') # O método replace procura todas letras 'U' na variável nome e substituí por '*'

print(nome) # aparecerá o nome digitado pelo usuário, com todas a substituições

```
## EXERCÍCIO 3
Uma escola de cursos de TI oferece vouchers para que os participantes possam assistir algumas aulas gratuitas de Python. Para isso o participante que deseja assistir as aulas gratuitas desse curso específico, deve fazer uma inscrição para receber o voucher.

Implemente um programa que armazene as inscrições para o curso. O programa deverá armazenar para cada inscrição: 
- Um código único para o voucher 
- Nome 
- E-mail 
- Telefone 
- Curso  
O programa deverá apresentar um menu de opções ao usuário:

1 – Inscrição:  ao selecionar essa opção, o usuário deverá ser capaz de informar todos os dados da inscrição.   O código do voucher deve ser preenchido automaticamente pelo sistema, e o usuário não deve ter a opção de alterar esse código; 

2 – Visualizar inscrição: ao selecionar essa opção, o programa deverá imprimir, na tela, para cada reserva, todos os dados dessa inscrição.  Caso nenhuma inscrição tenha sido cadastrada ao selecionar essa opção, o programa deverá exibir a mensagem “nenhuma inscrição cadastrada”.; 

0 – Encerrar: ao selecionar essa opção, o programa se encerra. 

Caso o usuário escolha uma opção que não conste no menu, o programa deverá exibir uma mensagem de erro, por exemplo, “Erro: digite uma opção válida!”. 

```
import random # biblioteca random, para gerar números pseudo-aleatórios

def bordamenui(x): # função para borda superior do menu
    print('°' * 10, x, '°' * 10)

def bordamenuf(): # função para borda inferior do menu
    print('°' * 26)

def bordalistai(x): # função para borda superior da lista de inscritos
    print('-' * 11, x, '-' * 11)

def bordalistaf(): # função para borda inferior da lista de inscritos
    print('-' * 42)

inscricoes = [] # lista que receberá o dicionário com as inscrições
cadastro = {} # dicionário que receberá as inscrições
voucher_sorteados = [] # lista que receberá os voucher sorteados

while True: # laço de repetição do menu
    print(' ')
    bordamenui('MENU')  # função da borda inicial do menu
    print('1 - Nova inscrição')
    print('2 - Visualizar inscrição')
    print('0 - Encerrar')
    bordamenuf() # função da borda final do menu
    escolha = input('\nPor favor, informe o que deseja fazer: ') # usuário informa sua opção

    while escolha not in '012': # enquanto não tiver '0 1 ou 2' na variável ecolha o programa continuará a pedir a opção para o usuário
        escolha = input('\nOpção inválida!\nPor favor digite:\n1 - Nova inscrição\n2 - Visualizar inscrição\n0 - Encerrar\nO que deseja fazer? ')

    if escolha == '0': # se usuário informar na variável escolha o número 0 encerra-se o programa
        print('Programa encerrado.')
        break # encerra-se o laço de repetição do menu

    elif escolha == '1': # se usuário informar na variável escolha o número 1 o programa solicitará dados para inscrição
        print('\n->> Nova inscrição\nPreencha corretamente os dados abaixo:\n')
        saida = True # variável booleana para garantir que não exista vouchers repetidos
        while saida: # cria-se um laço de repetição enquanto saída True
            n_voucher = random.randint(1, 10000) # n_voucher recebe um número aleatório
            if n_voucher not in voucher_sorteados: # se o número não tiver na lista voucher_sorteados
                voucher_sorteados.append(n_voucher) # n_voucher é adicionado na lista voucher_sorteados
                saida = False # variável booleana saída recebe False, encerra-se o laço de repetição

        cadastro['Voucher'] = n_voucher
        nome = input('Digite seu nome: ')
        while len(nome) == 0: # enquanto tamanho do nome for = 0 o programa continuará a pedir o nome para o usuário
            nome = input('Por favor, digite seu nome: ')
        email = input('Digite seu e-mail: ')
        while len(email) == 0: # enquanto tamanho do email for = 0 o programa continuará a pedir o email para o usuário
            email = input('Por favor, digite seu e-mail: ')
        telefone = input('Digite seu telefone: ')
        while not telefone.isnumeric(): # enquanto não tiver somente números o programa continuará a pedir telefone para o usuário
            telefone = input('Por favor digite somente números.\nTelefone: ')
        curso = input('Digite o nome do curso: ')
        while len(curso) == 0: # enquanto tamanho do curso for = 0 o programa continuará a pedir o curso para o usuário
            curso = input('Por favor, digite o nome do curso: ')
        cadastro['Nome'] = nome # nome é adicionado na chave 'Nome' no di-cionário cadastro
        cadastro['e-mail'] = email # email é adicionado na chave 'e-mail' no dicionário cadastro
        cadastro['Telefone'] = telefone # telefone é adicionado na chave 'Telefone' no dicionário cadastro
        cadastro['Curso'] = curso # curso é adicionado na chave 'Curso' no dicionário cadastro
        inscricoes.append(cadastro.copy()) # lista inscricoes recebe uma cópia do dicionário cadastro
        continue # retorna-se ao laço de repetição do menu

    elif escolha == '2': # se usuário escolher 2
        if len(inscricoes) == 0: # verifica se tamanho da lista inscricoes é = 0
            print('Nenhum inscrito cadastrado.') # se verdadeiro está mensagem aparecerá para o usuário
        else: # senão
            print(' ')
            bordalistai('Lista de Inscritos') # função borda inicial da lista de inscritos
            for i in inscricoes: # laço for na lista inscricoes
                for c, d in i.items(): # laço for na chave e dado do dicionário na lista inscricoes
                    print(f'{c} : {d}') # imprime chave : dado do dicionário
                print()
            bordalistaf() # função borda final da lista de inscritos
            continue # retorna ao laço de repetiçao do menu

print(inscricoes) # imprime a lista inscrições com os dicionários

```


  

