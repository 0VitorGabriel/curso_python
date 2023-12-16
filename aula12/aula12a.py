nome = str(input('Digite seu nome: '))

if nome == 'Gustavo':
    print('Que nome bonito voce tem!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome e bem popular no Brasil.')
elif nome in 'Ana Jessica Claudia Juliana':
    print('Belo nome feminino')

print(f'Tenha um bom dia, {nome}!')
