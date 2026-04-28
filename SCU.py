import json

try:
    with open('usuarios.json', 'r') as arquivo:
        usuarios = json.load(arquivo)
except FileNotFoundError:
    usuarios = []

# Função para salvar usuário no arquivo
def salvar_usuarios(usuarios):
    with open ('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo)


# Permite que o id continue correto após carregar JSON
if usuarios:
    usuario_id = max(u['id'] for u in usuarios) + 1
else:
    usuario_id = 1


# Função para cadastrar usuários - Opção 1
def cadastrar_usuario(usuarios, usuario_id):
    
    while True:
            usuario_nome = input('Digite seu usuário: ').strip()

            if len(usuario_nome) == 0:
                print('Campo vazio. Digite seu usuário corretamente!')
            else:
                break
        
    while True:
            usuario_email = input('Digite seu e-mail: ').strip().lower()

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
    
    salvar_usuarios(usuarios)
    
    return usuario_id


# Função para listar usuários - Opção 2
def listar_usuarios(usuarios):
    if not usuarios:
        print('Sem usuários cadastrados')
    else:
        for usuario in usuarios:
            print(f'id: {usuario["id"]} | nome: {usuario["nome"]} | email: {usuario["email"]}')



# Função para atualizar usuários - Opção 3
def atualizar_usuarios(usuarios):
    while True:
        try:
            id_digitado = int(input('Digite um id: '))
            break
        except ValueError:
            print('Digite um número válido!')
                
    usuario_encontrado = None

    for usuario in usuarios:
        if id_digitado == usuario['id']:
            usuario_encontrado = usuario
            break
    

    if usuario_encontrado:
        
        # Validação de nome
        while True:
            novo_nome_usuario = input('Digite seu novo nome de usuário: ').strip()

            if len(novo_nome_usuario) == 0:
                print('Nome de usuário inválido. DIgite novamente!')
            else:
                break
    
        # Validação de E-mail
        while True:
            novo_email_usuario = input('Digite seu novo e-mail:').strip().lower()

            if len(novo_email_usuario) == 0:
                print('E-mail inválido. Tente novamente!')
                continue

                
            email_duplicado = False


            for usuario in usuarios:
                if usuario['email'] == novo_email_usuario and usuario['id'] != usuario_encontrado['id']:
                    email_duplicado = True
                    break
                

            if email_duplicado:
                print('E-mail já cadastrado!')
            else:
                break

        # Atualização dos dados
        usuario_encontrado['nome'] = novo_nome_usuario
        usuario_encontrado['email'] = novo_email_usuario

        print('Usuário atualizado com sucesso!')
        salvar_usuarios(usuarios)
        
    else:
        print('Usuário não encontrado!')



# Função para deletar usuário - Opção 4
def deletar_usuario(usuarios):
    while True:
        try:
            usuario_digitado = int(input('Digite o id do usuário: '))
            break
        except ValueError:
            print('Digite um número válido')
            

    usuario_encontrado = None

    for usuario in usuarios:
        if usuario['id'] == usuario_digitado:
            usuario_encontrado = usuario
            break
                

    if usuario_encontrado:
        usuarios.remove(usuario_encontrado)
        print('Usuário removido com sucesso!') 

        salvar_usuarios(usuarios)
            
    else:
        print('Usuário não encontrado')


    
# Menu do Sistema de Cadastro de Usuários
while True:

    print('1 - Cadastrar usuário')
    print('2 - Listar usuário')
    print('3 - Atualizar Usuário')
    print('4 - Deletar Usuário')
    print('0 - Sair')

    
    opcao = input('Digite uma opção: ')

   
    if opcao == '1':
        usuario_id = cadastrar_usuario(usuarios, usuario_id)

    elif opcao == '2':
        listar_usuarios(usuarios)

    elif opcao == '3':
        atualizar_usuarios(usuarios)

    elif opcao == '4':
        deletar_usuario(usuarios)

    elif opcao == '0':
        print('Saindo...')
        break

    else:
        print('Opção inválida. Digite novamente!')