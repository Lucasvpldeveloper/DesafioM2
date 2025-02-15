nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

if idade <= 15:
    print(nome, 'Infelizmente você NÃO pode votar')
else:
    print(nome,'Você pode votar! vote com sabedoria')