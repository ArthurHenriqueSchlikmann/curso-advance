simbolo = input('Qual símbolo você deseja?: ')
linhas = int(input('Quantas linhas você deseja? '))
for i in range(1, linhas + 1):
        print(' ' * (linhas - i) + simbolo * i + simbolo * i)