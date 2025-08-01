from numpy import double

# Pede ao usuário o capital inicial, a taxa de juros e o tempo de aplicação
capitalInicial = int(input('Digite o capital inicial da aplicação: '))
taxaJuros = double(input('Digite a taxa de juros: ')) / 100
tempo = int(input('Digite o tempo de aplicação em anos: '))
# Calcula o montante final usando a fórmula do montante
montante = capitalInicial * (1 + taxaJuros) ** tempo
# Exibe o montante final
print('O montante após', tempo, 'anos é:', montante)