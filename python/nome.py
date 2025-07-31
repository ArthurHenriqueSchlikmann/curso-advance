nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
cor = input('Qual a sua cor favorita? ')
if(idade > 150):
    print('Você já viveu demais, considere descansar! LOL :)')
    print('Erro: Idade inválida.')
else:
    print('Olá,', nome, 'de', idade, 'anos, que tem a cor favorita', cor)