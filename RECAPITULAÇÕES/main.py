tipo_instalacao = str(input('Digite o tipo de instalação feita (para residencias digite R, para industrias digite I e digite C para comercios): '))
qtd_consumido = float(input('Digite a quantidade de kWh consumidas: '))

if tipo_instalacao == 'R' or tipo_instalacao == 'r':
    if qtd_consumido <= 500:
        tarifa = 0.40
    else:
        tarifa = 0.65
elif tipo_instalacao == 'I' or tipo_instalacao == 'i':
    if qtd_consumido <= 1000:
        tarifa = 0.55
    else:
        tarifa = 0.60
elif tipo_instalacao == 'C' or tipo_instalacao == 'c':
    if qtd_consumido <= 5000:
        tarifa = 0.55
    else:
        tarifa = 0.60
else:
    print('Digite R/I/C para calcularmos.')

preco_total = qtd_consumido * tarifa    

print(
    f'''
    Você digitou a opção {tipo_instalacao},
    Sua quantidade consumida foi de {qtd_consumido} kWh,
    Sua conta será no valor de R${preco_total:.2f} reais.
    ''')