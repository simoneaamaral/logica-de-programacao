nome = input('Digite um nome: ').upper() # usuário digita um nome, método upper converte o nome digitado para maiúsculo

print(nome) # aparecerá o nome digitado pelo usuário em maiúsculo


nome = nome.replace('A','@') # O método replace procura todas letras 'A' na variável nome e substituí por '@'
nome = nome.replace('E','&') # O método replace procura todas letras 'E' na variável nome e substituí por '&'
nome = nome.replace('I','!') # O método replace procura todas letras 'I' na variável nome e substituí por '!'
nome = nome.replace('O','#') # O método replace procura todas letras 'O' na variável nome e substituí por '#'
nome = nome.replace('U','*') # O método replace procura todas letras 'U' na variável nome e substituí por '*'

print(nome) # aparecerá o nome digitado pelo usuário, com todas a substituições