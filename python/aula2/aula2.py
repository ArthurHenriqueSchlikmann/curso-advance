exercicio = input('Qual é o exercício que você quer ver? DESAFIO = 6, EXERCÍCIO = 1, 2, 3, 4, 5: ')
#Sei usar if e else, e botei todos os exercícios em um programa, daí escolhe o exercício que quer ver
if exercicio == '1':
    nomes = ['Kauã', 'Anthony', 'Cenci', 'Erick', 'Guilherme', 'José', 'Matheus', 'Murilo', 'Nicolas', 'Arthur']
    print(nomes[0], 'é um professor de Python')
    print(nomes[6], 'perguntou o óbvio')
    print(nomes[3], 'Não gosta de Counter-Strike')
    print(nomes[1], 'não sei o que dizer sobre ele')
    print(nomes[2], 'também não sei desse potencinha')
    print(nomes[4], 'Conheço não')
    print(nomes[5], 'Existe?')
    print(nomes[7], 'tomou atividade extra')
    print(nomes[8], 'não conheço')
    print(nomes[9], 'I Use Arch BTW')
elif exercicio == '2':
    lista1 = [1, 2, 3, 4, 5]
    print(lista1)
    lista2 = [6, 7, 8, 9, 10]
    print(lista2)
    lista1.append(lista2[0:6])
    print(lista1)
elif exercicio == '3':
    comidas = ['Maionese', 'Churrasco', 'Hamburguer', 'Pizza', 'Linguiça','Queijo']
    print(comidas[0], 'é minha preferida')
    print(comidas[1], 'todo domingo tem churrasco')
    print(comidas[2], 'é gostoso')
    print(comidas[3], 'meu pai faz pizza muito boa') 
    print(comidas[4], 'adoro no pão')
    print(comidas[5], 'é uma comida muito boa, mas fica melhor derretido')
elif exercicio == '4':
    comidas = ['Maionese', 'Churrasco', 'Hamburguer', 'Pizza', 'Linguiça','Queijo']
    comida = comidas.pop(4)
    print('Matheus vai ganhar {comida}')
elif exercicio == '5':
    nomes = ['Kauã', 'Anthony', 'Cenci', 'Erick', 'Guilherme', 'José', 'Matheus', 'Murilo', 'Nicolas', 'Arthur']
    print(nomes[0].upper() , nomes[1].upper(), nomes[2].upper(), nomes[3].upper(), nomes[4].upper(), nomes[5].upper(), nomes[6].upper(), nomes[7].upper(), nomes[8].upper(), nomes[9].upper())
elif exercicio == '6':
    for i in range(499, 5001):
        print(i)