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
        continue # o programa retorna ao início do laço de repetição1