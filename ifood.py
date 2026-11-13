clientes = []
restaurantes = []
entregadores = []
pedidos = []

clientes.append({"id": 1, "nome": "João", "endereco": "Rua A, 1234", "telefone": "9898756909"})
restaurantes.append({"id": 1, "nome": "Pizzaria 3 parceiros", "endereco": "Rua B, 5678"})
entregadores.append({ "id": 1, "nome": "Maria", "veiculo": "Moto"})
pedidos.append({"cliente": clientes[0], "restaurante": restaurantes[0], "entregador": entregadores[0]})

novo_id_cliente = 2
novo_id_restaurante = 2
novo_id_entregador = 2
novo_id_pedido = 1

etapas = ["Aguardando confirmação do restaurante", "Pedido em preparo", "Pedido pronto para entrega", "Pedido a caminho", "Pedido entregue"]


while True:
    print("Bem-vindo ao iFood!")
    print("1.clientes")
    print("2.restaurantes")
    print("3.entregadores")
    print("4.pedidos")
    print("5.sair")
    opcao = input("escolha uma opção: ")

    if opcao == "1":
        print("\n1.cadastrar clientes")
        print("2.listar clientes")
        print("3.consultar por id")
        print("4.atualizar")
        print("5.excluir")
        print("6.voltar")
        op = input("escolha uma opção: ")

        if op == "1":
            nome = input("digite o nome do cliente: ")
            endereco = input("digite o endereço do cliente: ")
            telefone = input("digite o telefone do cliente: ")
            clientes.append({"id": novo_id_clientes, "nome": nome, "endereco": endereco, "telefone": telefone})
            print(f"Cliente {nome} cadastrado com sucesso!")
            novo_id_clientes += 1

        elif op in ("2", "3", "4", "5"):
            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                for cliente in clientes:
                    print(f"ID: {cliente['id']}, Nome: {cliente['nome']}, Endereço: {cliente['endereco']}, Telefone: {cliente['telefone']}")

        elif op == "6":
            continue

        else:
            print("Opção inválida.")

    elif opcao == "5":
        print("Até logo!")
        break

    elif op == "3":
        id_texto = input("ID do cliente: ")
        achou = False
        for clientes in clientes:
            if str(clientes["id"]) == id_texto:
                print("Nome:", clientes["nome"])
                print("Endereço:", clientes["endereco"])
                print("Telefone:", clientes["telefone"])
                achou = True
        if achou == False:
                    print("Cliente não encontrado.")
 
    elif op == "5":
        id_texto = input("id do cliente para excluir: ")
        achou = False
        for cliente in clientes:
            if str(cliente["id"]) == id_texto:
                clientes.remove(cliente)
                achou = True
                print(f"Cliente {cliente['nome']} excluído com sucesso!")
                break
            if achou == False:
                print("Cliente não encontrado.")
    elif op == "false":
        print("Opção inválida.")


    elif opcao == "2":
        while True:
            print("1.cadastrar")
            print("2.listar")
            print("3.consultar por id")
            print("4.atualizar")
            print("5.apagar")
            print("0.voltar")
            op = input("Escolha uma opção:")

            if op == "1":
                nome = input("nome do restaurante: ")
                categoria = input("categoria do restaurante: ")
                endereco = input("endereço do restaurante: ")
                restaurante = {"id": novo_id_restaurante, "nome": nome, "categoria": categoria, "endereco": endereco}
                restaurantes.append(restaurante)
                print(f"{nome} cadastrado com sucesso!")
                novo_id_restaurante += 1

            elif op == "2":
                if len(restaurantes) == 0:
                    print("Nenhum restaurante cadastrado.")
                else:
                    for restaurante in restaurantes:
                        print(f"ID: {restaurante['id']}, nome: {restaurante['nome']}, categoria: {restaurante['categoria']}, endereço: {restaurante['endereco']}")

            elif op == "3":
                id_texto = input("ID do restaurante: ")
                achou = False
                for restaurante in restaurantes:
                    if str(restaurante["id"]) == id_texto:
                        print(f"ID: {restaurante['id']}, nome: {restaurante['nome']}, categoria: {restaurante['categoria']}, endereço: {restaurante['endereco']}")
                        achou = True
                        break
                if not achou:
                    print("Restaurante não encontrado.")

    elif op == "4":
            id_texto = input("ID do restaurante para atualizar: ")
            achou = False
            for restaurante in restaurantes:
                if str(restaurante["id"]) == id_texto:
                    nome = input("novo nome do restaurante: ")
                    categoria = input("nova categoria do restaurante: ")
                    endereco = input("novo endereço do restaurante: ")
                    restaurante["nome"] = nome
                    restaurante["categoria"] = categoria
                    restaurante["endereco"] = endereco
                    print(f"Restaurante {nome} atualizado com sucesso!")
                    achou = True
                    break
            if not achou:
                print("Restaurante não encontrado.")
    elif op == "5":
        id_texto = input("ID do restaurante para excluir: ")
        achou = False
        for restaurante in restaurantes:
            if str(restaurante["id"]) == id_texto:
                restaurantes.remove(restaurante)
                achou = True
                print(f"Restaurante {restaurante['nome']} excluído com sucesso!")
                break