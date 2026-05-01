from storage import salvar_usuarios

def cadastrar_usuarios(usuarios, usuario_id):
    while True:
        nome = input('Digite seu usuário: ').strip()

        if nome:
            break
        print('Nome inválido!')
    
    while True:
        email = input('Digite seu e-mail: ').strip().lower()

        if not email:
            print('E-mail inválido!')
            continue

        
        email_existente = False


        for usuario in usuarios:
            if usuario['email'] == email:
                email_existente = True
                break

        
        if email_existente:
            print('E-mail já cadastrado')
        else:
            break

        
    usuario = {
        'id': usuario_id,
        'nome': nome,
        'email': email  
    }

    usuarios.append(usuario)
    salvar_usuarios(usuarios)

    print(f'Usuário cadastrado com sucesso! (ID: {usuario_id})')

    return usuario_id + 1



def listar_usuarios(usuarios):
    if not usuarios:
        print('Sem usuários cadastrados')
        return
    
    print('\n---- LISTA DE USUÁRIOS ----\n')

    for usuario in usuarios:
        print(f'id: {usuario["id"]} | nome: {usuario["nome"]} | email: {usuario["email"]}')
              


def atualizar_usuarios(usuarios):
    try:
        id_digitado = int(input('Digite um id: '))
    except ValueError:
        print('Digite um número válido')
        return

    
    usuario_encontrado = None


    for usuario in usuarios:
        if usuario['id'] == id_digitado:
            usuario_encontrado = usuario
            break
            
    
    if not usuario_encontrado:
        print('Usuário não encontrado')
        return

    
    while True:
        novo_nome = input('Digite o novo nome: ').strip()
        
        if novo_nome:
            break
        print('Nome inválido')

    while True:
        novo_email = input('Digite o novo email: ').strip().lower()


        if not novo_email:
            print('E-mail inválido')
            continue
        

        email_duplicado = False


        for usuario in usuarios:
            if usuario['email'] == novo_email and usuario['id'] != usuario_encontrado['id']:
                email_duplicado = True
                break

        
        if email_duplicado:
            print('Email já cadastrado!')
        else:
            break
        
    usuario_encontrado['nome'] = novo_nome
    usuario_encontrado['email'] = novo_email
    
    salvar_usuarios(usuarios)
    print('Usuário atualizado com sucesso!')



def deletar_usuario(usuarios):
    try:
        id_digitado = int(input('Digite o id do usuário: '))
    except ValueError:
        print('Digite um número válido!')
        return

    
    usuario_encontrado = None


    for usuario in usuarios:
        if usuario['id'] == id_digitado:
            usuario_encontrado = usuario
            break
        
    
    if not usuario_encontrado:
        print('Usuário não encontrado')
        return
    

    confirmacao = input('Tem certeza que deseja excluir s/n: ').lower()


    if confirmacao != 's':
        print('Operação cancelada')
        return
    

    usuarios.remove(usuario_encontrado)
    salvar_usuarios(usuarios)

    print('Usuário removido com sucesso!')