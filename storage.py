import json

ARQUIVO = 'usuarios.json'

def carregar_usuarios():
    try:
        with open(ARQUIVO, 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
            return []

def salvar_usuarios(usuarios):
    with open(ARQUIVO, 'w') as arquivo:
        json.dump(usuarios, arquivo, indent=4)

