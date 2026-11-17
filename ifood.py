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
restaurantes.append({"id": 1, "nome": "Pizzaria", "endereco": "Rua B, 5678", "cardapio": cardapio_pizzaria})
restaurantes.append({"id": 2, "nome": "Hamburgueria", "endereco": "Av. C, 100", "cardapio": cardapio_hamburgueria})
restaurantes.append({"id": 3, "nome": "Churrascaria", "endereco": "Rua D, 200", "cardapio": cardapio_churrascaria})
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
            opcao_submenu = input("Escolha uma opção: ")

            if opcao_submenu == "1":
                nome = input("Nome: ")
                endereco = input("Endereço: ")
                telefone = input("Telefone: ")
                clientes.append({"id": novo_id_cliente, "nome": nome, "endereco": endereco, "telefone": telefone})
                print("Cliente", nome, "cadastrado com ID", novo_id_cliente)
                novo_id_cliente = novo_id_cliente + 1

            elif opcao_submenu == "2":
                if len(clientes) == 0:
                    print("Nenhum cliente cadastrado.")
                else:
                    for cliente in clientes:
                        print(cliente["id"], "-", cliente["nome"], "|", cliente["endereco"], "|", cliente["telefone"])

            elif opcao_submenu == "3":
                id_busca = input("ID do cliente: ")
                achou = False
                for cliente in clientes:
                    if str(cliente["id"]) == id_busca:
                        achou = True
                        print("Nome:", cliente["nome"])
                        print("Endereço:", cliente["endereco"])
                        print("Telefone:", cliente["telefone"])
                if achou == False:
                    print("Cliente não encontrado.")

            elif opcao_submenu == "4":
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

            elif opcao_submenu == "5":
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

            elif opcao_submenu == "0":
                break
            else:
                print("Opção inválida!")

    elif opcao == "2":
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

            if opcao_submenu == "1":
                nome = input("Nome do restaurante: ")
                endereco = input("Endereço: ")
                restaurantes.append({"id": novo_id_restaurante, "nome": nome, "endereco": endereco, "cardapio": []})
                print("Restaurante", nome, "cadastrado com ID", novo_id_restaurante)
                print("Use a opção 6 para adicionar pratos ao cardápio.")
                novo_id_restaurante = novo_id_restaurante + 1

            elif opcao_submenu == "2":
                if len(restaurantes) == 0:
                    print("Nenhum restaurante cadastrado.")
                else:
                    for restaurante in restaurantes:
                        print(restaurante["id"], "-", restaurante["nome"], "|", restaurante["endereco"], "|", len(restaurante["cardapio"]), "pratos")

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
                            numero = 1
                            for prato in restaurante["cardapio"]:
                                print(" ", numero, "-", prato["nome"], "| R$", prato["preco"])
                                numero = numero + 1
                if achou == False:
                    print("Restaurante não encontrado.")

            elif opcao_submenu == "4":
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

            elif opcao_submenu == "6":
                id_busca = input("ID do restaurante: ")
                achou = False
                for restaurante in restaurantes:
                    if str(restaurante["id"]) == id_busca:
                        achou = True
                        cardapio = restaurante["cardapio"]

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
                                    cardapio.append({"nome": nome_prato, "preco": float(preco_texto)})
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
                                if numero_texto.isdigit():
                                    if int(numero_texto) >= 1 and int(numero_texto) <= len(cardapio):
                                        numero_valido = True
                                if numero_valido:
                                    prato = cardapio[int(numero_texto) - 1]
                                    print("(Aperte Enter para manter o valor atual)")
                                    novo = input("Nome [" + prato["nome"] + "]: ")
                                    if novo != "":
                                        prato["nome"] = novo
                                    novo = input("Preço [" + str(prato["preco"]) + "]: ")
                                    novo = novo.replace(",", ".")
                                    if novo != "":
                                        if novo.replace(".", "", 1).isdigit():
                                            prato["preco"] = float(novo)
                                        else:
                                            print("Preço inválido, o preço antigo foi mantido.")
                                    print("Prato atualizado!")
                                else:
                                    print("Número inválido.")

                            elif opcao_cardapio == "4":
                                numero_texto = input("Número do prato a remover: ")
                                numero_valido = False
                                if numero_texto.isdigit():
                                    if int(numero_texto) >= 1 and int(numero_texto) <= len(cardapio):
                                        numero_valido = True
                                if numero_valido:
                                    cardapio.pop(int(numero_texto) - 1)
                                    print("Prato removido!")
                                else:
                                    print("Número inválido.")

                            elif opcao_cardapio == "0":
                                break
                            else:
                                print("Opção inválida!")
                if achou == False:
                    print("Restaurante não encontrado.")

            elif opcao_submenu == "0":
                break
            else:
                print("Opção inválida!")

    elif opcao == "3":
        while True:
            print("\n--- ENTREGADORES ---")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Consultar por ID")
            print("4 - Atualizar")
            print("5 - Excluir")
            print("0 - Voltar")
            opcao_submenu = input("Escolha uma opção: ")

            if opcao_submenu == "1":
                nome = input("Nome do entregador: ")
                veiculo = input("Veículo (moto, bike, carro): ")
                entregadores.append({"id": novo_id_entregador, "nome": nome, "veiculo": veiculo})
                print("Entregador", nome, "cadastrado com ID", novo_id_entregador)
                novo_id_entregador = novo_id_entregador + 1

            elif opcao_submenu == "2":
                if len(entregadores) == 0:
                    print("Nenhum entregador cadastrado.")
                else:
                    for entregador in entregadores:
                        print(entregador["id"], "-", entregador["nome"], "|", entregador["veiculo"])

            elif opcao_submenu == "3":
                id_busca = input("ID do entregador: ")
                achou = False
                for entregador in entregadores:
                    if str(entregador["id"]) == id_busca:
                        achou = True
                        print("Nome:", entregador["nome"])
                        print("Veículo:", entregador["veiculo"])
                if achou == False:
                    print("Entregador não encontrado.")

            elif opcao_submenu == "4":
                id_busca = input("ID do entregador a atualizar: ")
                achou = False
                for entregador in entregadores:
                    if str(entregador["id"]) == id_busca:
                        achou = True
                        print("(Aperte Enter para manter o valor atual)")
                        novo = input("Nome [" + entregador["nome"] + "]: ")
                        if novo != "":
                            entregador["nome"] = novo
                        novo = input("Veículo [" + entregador["veiculo"] + "]: ")
                        if novo != "":
                            entregador["veiculo"] = novo
                        print("Entregador atualizado!")
                if achou == False:
                    print("Entregador não encontrado.")

            elif opcao_submenu == "5":
                id_busca = input("ID do entregador a excluir: ")
                achou = False
                for entregador in entregadores:
                    if str(entregador["id"]) == id_busca:
                        achou = True
                        tem_pedido = False
                        for pedido in pedidos:
                            if pedido["entregador_id"] == entregador["id"]:
                                tem_pedido = True
                        if tem_pedido:
                            print("Não dá para excluir: este entregador tem pedidos.")
                        else:
                            entregadores.remove(entregador)
                            print("Entregador excluído!")
                        break
                if achou == False:
                    print("Entregador não encontrado.")

            elif opcao_submenu == "0":
                break
            else:
                print("Opção inválida!")

    elif opcao == "4":
        while True:
            print("\n--- PEDIDOS ---")
            print("1 - Fazer pedido")
            print("2 - Listar")
            print("3 - Consultar por ID")
            print("4 - Atualizar status")
            print("5 - Excluir")
            print("0 - Voltar")
            opcao_submenu = input("Escolha uma opção: ")

            if opcao_submenu == "1":
                id_cliente = input("ID do cliente: ")
                cliente_achado = None
                for cliente in clientes:
                    if str(cliente["id"]) == id_cliente:
                        cliente_achado = cliente

                if cliente_achado == None:
                    print("Cliente não encontrado.")
                else:
                    id_restaurante = input("ID do restaurante: ")
                    restaurante_achado = None
                    for restaurante in restaurantes:
                        if str(restaurante["id"]) == id_restaurante:
                            restaurante_achado = restaurante

                    if restaurante_achado == None:
                        print("Restaurante não encontrado.")
                    elif len(restaurante_achado["cardapio"]) == 0:
                        print("Este restaurante ainda não tem cardápio.")
                    else:
                        id_entregador = input("ID do entregador: ")
                        entregador_achado = None
                        for entregador in entregadores:
                            if str(entregador["id"]) == id_entregador:
                                entregador_achado = entregador

                        if entregador_achado == None:
                            print("Entregador não encontrado.")
                        else:
                            cardapio = restaurante_achado["cardapio"]
                            itens = []
                            total = 0.0

                            while True:
                                print("\n--- CARDÁPIO:", restaurante_achado["nome"], "---")
                                numero = 1
                                for prato in cardapio:
                                    print(numero, "-", prato["nome"], "| R$", prato["preco"])
                                    numero = numero + 1
                                escolha = input("Número do prato (0 para finalizar): ")

                                if escolha == "0":
                                    break
                                elif escolha.isdigit() and int(escolha) >= 1 and int(escolha) <= len(cardapio):
                                    prato = cardapio[int(escolha) - 1]
                                    itens.append({"nome": prato["nome"], "preco": prato["preco"]})
                                    total = total + prato["preco"]
                                    print(prato["nome"], "adicionado! Total até agora: R$", round(total, 2))
                                else:
                                    print("Número inválido.")

                            if len(itens) == 0:
                                print("Pedido vazio, nada foi criado.")
                            else:
                                pedidos.append({"id": novo_id_pedido, "cliente_id": cliente_achado["id"], "restaurante_id": restaurante_achado["id"], "entregador_id": entregador_achado["id"], "itens": itens, "total": total, "status": "Preparando"})
                                print("Pedido", novo_id_pedido, "criado! Total: R$", round(total, 2))
                                novo_id_pedido = novo_id_pedido + 1

            elif opcao_submenu == "2":
                if len(pedidos) == 0:
                    print("Nenhum pedido feito.")
                else:
                    for pedido in pedidos:
                        print("Pedido", pedido["id"], "| Cliente", pedido["cliente_id"], "| Restaurante", pedido["restaurante_id"], "| R$", round(pedido["total"], 2), "|", pedido["status"])

            elif opcao_submenu == "3":
                id_busca = input("ID do pedido: ")
                achou = False
                for pedido in pedidos:
                    if str(pedido["id"]) == id_busca:
                        achou = True
                        print("Pedido:", pedido["id"])
                        print("Cliente ID:", pedido["cliente_id"])
                        print("Restaurante ID:", pedido["restaurante_id"])
                        print("Entregador ID:", pedido["entregador_id"])
                        print("Itens:")
                        for item in pedido["itens"]:
                            print("  -", item["nome"], "| R$", item["preco"])
                        print("Total: R$", round(pedido["total"], 2))
                        print("Status:", pedido["status"])
                if achou == False:
                    print("Pedido não encontrado.")

            elif opcao_submenu == "4":
                id_busca = input("ID do pedido: ")
                achou = False
                for pedido in pedidos:
                    if str(pedido["id"]) == id_busca:
                        achou = True
                        print("Status atual:", pedido["status"])
                        print("1 - Preparando")
                        print("2 - Saiu para entrega")
                        print("3 - Entregue")
                        print("4 - Cancelado")
                        novo_status = input("Novo status: ")
                        if novo_status == "1":
                            pedido["status"] = "Preparando"
                        elif novo_status == "2":
                            pedido["status"] = "Saiu para entrega"
                        elif novo_status == "3":
                            pedido["status"] = "Entregue"
                        elif novo_status == "4":
                            pedido["status"] = "Cancelado"
                        else:
                            print("Opção inválida, status mantido.")
                        print("Status do pedido:", pedido["status"])
                if achou == False:
                    print("Pedido não encontrado.")

            elif opcao_submenu == "5":
                id_busca = input("ID do pedido a excluir: ")
                achou = False
                for pedido in pedidos:
                    if str(pedido["id"]) == id_busca:
                        achou = True
                        pedidos.remove(pedido)
                        print("Pedido excluído!")
                        break
                if achou == False:
                    print("Pedido não encontrado.")

            elif opcao_submenu == "0":
                break
            else:
                print("Opção inválida!")

    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")