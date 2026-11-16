clientes = []
restaurantes = []
entregadores = []
pedidos = []

cardapio_pizzaria = [
    {"nome": "Pizza de Calabresa", "preco": 45.0},
    {"nome": "Pizza de Mussarela", "preco": 40.0},
    {"nome": "Pizza Portuguesa", "preco": 48.0},
    {"nome": "Refrigerante 2L", "preco": 12.0},
]

cardapio_hamburgueria = [
    {"nome": "X-Burger", "preco": 25.0},
    {"nome": "X-Bacon", "preco": 30.0},
    {"nome": "Batata Frita", "preco": 15.0},
    {"nome": "Milkshake", "preco": 18.0},
]

cardapio_churrascaria = [
    {"nome": "Picanha (porção)", "preco": 79.9},
    {"nome": "Costela (porção)", "preco": 69.9},
    {"nome": "Arroz, farofa e vinagrete", "preco": 20.0},
    {"nome": "Suco natural", "preco": 10.0},
]

clientes.append({"id": 1, "nome": "João", "endereco": "Rua A, 1234", "telefone": "9898756909"})
restaurantes.append({"id": 1, "nome": "Pizzaria", "endereco": "Rua B, 5678","cardapio": cardapio_pizzaria})
restaurantes.append({"id": 2, "nome": "Hamburgueria", "endereco": "Av. C, 100","cardapio": cardapio_hamburgueria})
restaurantes.append({"id": 3, "nome": "Churrascaria", "endereco": "Rua D, 200","cardapio": cardapio_churrascaria})
entregadores.append({"id": 1, "nome": "Maria", "veiculo": "Moto"})


novo_id_cliente = 2
novo_id_restaurante = 4
novo_id_entregador = 2
novo_id_pedido = 1

while True:
    print("\n ---BEM VINDO AO IFOOD---")
    print("1 - Clientes")
    print("2 - Restaurantes")
    print("3 - Entregadores")
    print("4 - Pedidos")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            print("\n--- CLIENTES ---")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Consultar por ID")
            print("4 - Atualizar")
            print("5 - Excluir")
            print("0 - Voltar")
            opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            endereco = input("Endereço: ")
            telefone = input("Telefone: ")
            clientes.append({"id": novo_id_cliente, "nome": nome,"endereco": endereco, "telefone": telefone})
        print("Cliente", nome, "cadastrado com ID", novo_id_cliente)
        novo_id_cliente = novo_id_cliente + 1

    elif opcao == "2":
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(cliente["id"], "-", cliente["nome"], "|", cliente["endereco"], "|", cliente["telefone"])

    elif opcao == "3":
         id_busca = input("ID do cliente: ")
         achou = False
    for cliente in clientes:
        if str(cliente["id"]) == id_busca:
            print("Nome:", cliente["nome"])
            print("Endereço:", cliente["endereco"])
            print("Telefone:", cliente["telefone"])
        achou = True
    if achou == False:
            print("Cliente não encontrado.")

    elif opcao == "4":
        id_busca = input("ID do cliente a atualizar: ")
        achou = False
        for cliente in clientes:
            if str(cliente["id"]) == id_busca:
                achou = True
                print("(Aperte Enter para manter o valor atual)")
                novo = input("Nome [" + cliente["nome"] + "]: ")
            if novo != "":
                cliente["nome"] = novo
            novo = input("Endereço [" + cliente["endereco"] + "]: ")
            if novo != "":
                cliente["endereco"] = novo
                novo = input("Telefone [" + cliente["telefone"] + "]: ")
            if novo != "":
                cliente["telefone"] = novo
                print("Cliente atualizado!")
        if achou == False:
            print("Cliente não encontrado.")


    elif opcao == "5":
        id_busca = input("ID do cliente a excluir: ")
        achou = False
        for cliente in clientes:
            if str(cliente["id"]) == id_busca:
                achou = True
                tem_pedido = False
            for pedido in pedidos:
                if pedido["cliente_id"] == cliente["id"]:
                    tem_pedido = True
            if tem_pedido:
                    print("Não dá para excluir: este cliente tem pedidos.")
            else:
                clientes.remove(cliente)
                print("Cliente excluído!")
                break
            if achou == False:
                    print("Cliente não encontrado.")

    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

while True:
        print("\n--- RESTAURANTES ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Consultar por ID (mostra o cardápio)")
        print("4 - Atualizar")
        print("5 - Excluir")
        print("6 - Gerenciar cardápio")
        print("0 - Voltar")
        opcao_submenu = input("Escolha uma opção: ")

if opcao == "1":
    nome = input("Nome do restaurante: ")
    endereco = input("Endereço: ")
    restaurantes.append({"id": novo_id_restaurante, "nome": nome,"endereco": endereco, "cardapio": []})
    print("Restaurante", nome, "cadastrado com ID", novo_id_restaurante)
    print("Use a opção 6 para adicionar pratos ao cardápio.")
    novo_id_restaurante = novo_id_restaurante + 1

elif opcao_submenu == "2":
    if len(restaurantes) == 0:
        print("Nenhum restaurante cadastrado.")
    else:
        for restaurante in restaurantes:
            print(restaurante["id"], "-", restaurante["nome"], "|",restaurante["endereco"], "|",
                len(restaurante["cardapio"]), "pratos")

elif opcao_submenu == "3":
    id_busca = input("ID do restaurante: ")
    achou = False
    for restaurante in restaurantes:
        if str(restaurante["id"]) == id_busca:
            achou = True
            print("Nome:", restaurante["nome"])
            print("Endereço:", restaurante["endereco"])
            print("Cardápio:")
        if len(restaurante["cardapio"]) == 0:
            print("  (vazio)")
        else:
            numero = 1   # contador para numerar os pratos
        for prato in restaurante["cardapio"]:
            print(" ", numero, "-", prato["nome"], "| R$", prato["preco"])
            numero = numero + 1
        if achou == False:
           print("Restaurante não encontrado.")

elif opcao == "4":
    id_busca = input("ID do restaurante a atualizar: ")
    achou = False
    for restaurante in restaurantes:
        if str(restaurante["id"]) == id_busca:
            achou = True
        print("(Aperte Enter para manter o valor atual)")
        novo = input("Nome [" + restaurante["nome"] + "]: ")
        if novo != "":
            restaurante["nome"] = novo
        novo = input("Endereço [" + restaurante["endereco"] + "]: ")
        if novo != "":
            restaurante["endereco"] = novo
        print("Restaurante atualizado!")
    if achou == False:
        print("Restaurante não encontrado.")

elif opcao_submenu == "5":
    id_busca = input("ID do restaurante a excluir: ")
    achou = False
    for restaurante in restaurantes:
        if str(restaurante["id"]) == id_busca:
            achou = True
            tem_pedido = False
            for pedido in pedidos:
                if pedido["restaurante_id"] == restaurante["id"]:
                    tem_pedido = True
            if tem_pedido:
                print("Não dá para excluir: este restaurante tem pedidos.")
            else:
                restaurantes.remove(restaurante)
                print("Restaurante excluído!")
            break
    if achou == False:
        print("Restaurante não encontrado.")

elif opcao == "6":
    id_busca = input("ID do restaurante: ")
    achou = False
    for restaurante in restaurantes:
        if str(restaurante["id"]) == id_busca:
           achou = True

           while True:
                print("\n--- CARDÁPIO:", restaurante["nome"], "---")
                print("1 - Adicionar prato")
                print("2 - Listar pratos")
                print("3 - Atualizar prato")
                print("4 - Remover prato")
                print("0 - Voltar")
                opcao_cardapio = input("Escolha uma opção: ")

                if opcao_cardapio == "1":
                    nome_prato = input("Nome do prato: ")
                    preco_texto = input("Preço (R$): ")
                    preco_texto = preco_texto.replace(",", ".")
                    if preco_texto.replace(".", "", 1).isdigit():
                        prato_novo = {"nome": nome_prato, "preco": float(preco_texto)}
                        cardapio.append(prato_novo)
                        print("Prato adicionado!")
                    else:
                        print("Preço inválido. Digite só números.")

                elif opcao_cardapio == "2":
                    if len(cardapio) == 0:
                        print("Cardápio vazio.")
                    else:
                        numero = 1
                        for prato in cardapio:
                            print(numero, "-", prato["nome"], "| R$", prato["preco"])
                            numero = numero + 1
                
                elif opcao_cardapio == "3":
                    numero_texto = input("Número do prato a atualizar: ")
                    numero_valido = False
                    quantidade = len(cardapio)
                    if numero_texto.isdigit():
                        if int(numero_texto) >= 1 and int(numero_texto) <= quantidade:
                            numero_valido = True
                        if numero_valido:
                            prato = cardapio[int(numero_texto) - 1]
                            print("(Aperte Enter para manter o valor atual)")
                            novo = input("Nome [" + prato["nome"] + "]: ")
                            
                




