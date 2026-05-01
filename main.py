from storage import carregar_usuarios
from usuarios import (
    cadastrar_usuarios,
    listar_usuarios,
    atualizar_usuarios,
    deletar_usuario
)


usuarios = carregar_usuarios()


if usuarios:
    usuario_id = max(u['id'] for u in usuarios) + 1
else:
    usuario_id = 1



while True:

    print('\n==== SISTEMA DE USUÁRIOS ====\n')
    print('[1] - Cadastrar usuário')
    print('[2] - Listar usuários')
    print('[3] - Atualizar usuário')
    print('[4] - Deletar usuário')
    print('[0] - Sair\n')


    try:
        opcao = int(input('Digite uma opção: '))
    except ValueError:
        print('Digite um número válido')
        continue



    if opcao == 1:
        usuario_id = cadastrar_usuarios(usuarios, usuario_id)
    
    elif opcao == 2:
        listar_usuarios(usuarios)
    
    elif opcao == 3:
        atualizar_usuarios(usuarios)
    
    elif opcao == 4:
        deletar_usuario(usuarios)
    
    elif opcao == 0:
        print('Saindo...')
        break

    else:
        print('Opção inválida')