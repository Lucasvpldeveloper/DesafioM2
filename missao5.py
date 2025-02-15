senhaCorreta = 'Python123'
tentativaDeSenha = str(input('Digite a senha para acessar o cofre: '))

if tentativaDeSenha == senhaCorreta:
    print('Acesso liberado!')
else: 
    print('Acesso negado!')