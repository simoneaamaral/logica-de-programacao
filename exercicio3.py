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