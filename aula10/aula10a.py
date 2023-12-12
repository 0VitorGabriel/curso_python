nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
print(f'A sua media foi {media:.1f}')

print('aprovado' if media >= 6.0 else 'reprovado')
