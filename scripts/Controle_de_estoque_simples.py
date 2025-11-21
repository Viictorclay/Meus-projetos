import json
import os
estoque = []

def clear_system():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_estoque():
    global estoque
    if os.path.exists('estoque.json'):
        with open('estoque.json','r') as arquivo:
            estoque = json.load(arquivo)


    

def cadastrar_produto():
    print('\n === Cadastro de Produto ===')
    codigo = int(input(' Código do produto: '))
    nome = input(' Nome do produto')
    quantidade = int(input(' Quantidade em estoque: '))
    preco = float(input(' Preço do produto: R$ '))

    produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }


    estoque.append(produto)
    print(' ✅ Produto cadastrado com sucesso!')

def listar_produtos():
    if not estoque:
        print('\n ⚠️ Nenhum produto cadastrado.')
    else:
        print('\n === Lista de produtos ===')
        for prod in estoque:
            print(f" Código: {prod['codigo']} | Nome: {prod['nome']} | Quantidade: {prod['quantidade']} | Preço: {prod['preco']}")

def buscar_produto():
    cod = int(input(' Digite o código do produto: '))
    for prod in estoque:
        if prod["codigo"] == cod:
            print(f' Produto encotrado: {prod}')
            return
    print(' ❌ Produto não encontrado.')

def editar_quantidade():
    cod = int(input(' Digite o código do produto: '))
    for prod in estoque:
        if prod["codigo"] == cod:
            nova_qtd = int(input(' Nova quantidade: '))
            prod["quantidade"] = nova_qtd
            print(' Quantidade atualizada.')
            return

def remover_produto():
    cod = int(input(' Código do produto: '))
    for prod in estoque:
        if prod["codigo"] == cod:
            estoque.remove(prod)
            print(' Produto removido com sucesso.')
            return
    print(' ❌ Produto não encontrado.')

def salvar_sair():
    with open('estoque.json', 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)      
    print(' Estoque salvo com sucesso!')
    print('                                  Fechando programa...')
    exit()
# PROGRMA PRINCIPAL

def menu():
    carregar_estoque()
    while True:
        
        print("\n=== Menu Estoque ===\n")
        print("[1] Cadastrar produto")
        print("[2] Listar produtos")
        print("[3] Buscar produto por código")
        print("[4] Editar quantidade")
        print("[5] Remover produto")
        print("[6] Salvar e sair")
        opcao = input(" \n Escolha uma opção: ")
        clear_system()

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            editar_quantidade()
        elif opcao == "5":
            remover_produto()
        elif opcao == "6":
            salvar_sair()
            break
        else:
            print("⚠️ Opção inválida.")

menu()