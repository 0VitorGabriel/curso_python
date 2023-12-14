nome = 'Guanabara'

cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'preto_branco': '\033[7;30m'
}

print(f'Ola, e um prazer te conhcer, {cores["azul"]}{nome}{cores["limpa"]}!!!')
