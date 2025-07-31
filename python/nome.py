# Faz um questionário sobre a vida do usuário
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
cor = input('Qual a sua cor favorita? ')
if(idade > 150):
    # Se a idade for maior que 150, exibe uma mensagem de erro meme
    print('Você já viveu demais, considere descansar! LOL :)')
    print('Erro: Idade inválida.')
else:
    # Se a idade for válida, exibe uma mensagem de saudação, com nome, idade e cor favorita
    print('Olá,', nome, 'de', idade, 'anos, que tem a cor favorita', cor)