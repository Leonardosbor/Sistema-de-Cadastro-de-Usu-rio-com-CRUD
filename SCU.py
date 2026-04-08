usuarios = []
usuario_id = 1

while True:

    print('1 - Cadastrar uruário')
    print('2 - Listar usuário')
    print('3 - Atualizar Usuário')
    print('4 - Deletar Usuário')
    print('5 - Sair')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        
        while True:
            usuario_nome = input('Digite seu usuário: ')

            if len(usuario_nome) == 0:
                print('Campo vazio. Digite seu usuário corretamente!')
            else:
                break
        
        while True:
            usuario_email = input('Digite seu e-mail: ')

            if len(usuario_email) == 0:
                print('Campo vazio. Digite seu e-mail corretamente!')
                continue
        

            email_existente = False

            for usuario in usuarios:
                if usuario['email'] == usuario_email:
                    email_existente = True
                    break
            
            if email_existente:
                print('E-mail já cadastrado')
            else:
                break
                
        usuario = {
            'id': usuario_id,
            'nome': usuario_nome,
            'email': usuario_email
        }

        usuarios.append(usuario)
        print('Usuário cadastrado com sucesso!')
        usuario_id += 1

        
    
    elif opcao == '2':
        if len(usuarios) == 0:
            print('Sem usuários cadastrados')
        else:
            for usuario in usuarios:
                print(f'id: {usuario["id"]} | nome: {usuario["nome"]} | email: {usuario["email"]}')


    elif opcao == '3':

        while True:

            id_digitado = int(input('Digite um ID: '))

            for usuario in usuarios:
                if id_digitado == usuario['id']:

                    novo_nome_usuario = input('Digite um novo usuário: ')
                    novo_email_usuario = input('Digite um novo email para o usuário: ')

                    usuario_nome = novo_nome_usuario
                    usuario_email = novo_email_usuario

                else:
                    print('id não encontrado')
                    break    

                    

                






    elif opcao == '4':
        print('Usuário deletado com sucesso!')

    elif opcao == '5':
        print('Saindo...')
        break

    else:
        print('Opção inválida. Digite novamente!')