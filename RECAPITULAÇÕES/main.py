# Listas, dicts, tuplas, conjuntos

import os
os.system("cls")

senha = 1234
chance = 0

while chance < 3:
    try:
        pedir_senha = int(input('Digite a senha, só é permitido valores inteiros e você só tem 3 tentativas: '))
        if pedir_senha != senha:
            chance += 1
            print(f'Não é essa a senha, essa foi sua {chance} chance')            
            if chance == 3:
                print('Usuário bloqueado!')
                break
        else:
            print('Acertou sua senha é:', senha)
            break
    except ValueError:
        chance += 1
        print(f'Só aceitamos números inteiros, você usou a sua {chance} chance')
        if chance == 3:
            print('Usuário bloqueado!')
            break 