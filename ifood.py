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
    print("1. clientes")
    print("2. restaurantes")
    print("3. entregadores")
    print("4. pedidos")
    print("5. sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. consultar por id")
        print("4. atualizar")
        print("5. excluir")
        print("6. voltar")
        op = input("Escolha uma opção: ")

        if op == "1":
            nome = input("Digite o nome do cliente: ")
            endereco = input("Digite o endereço do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            clientes.append({"id": novo_id_cliente, "nome": nome, "endereco": endereco, "telefone": telefone})
            print(f"Cliente {nome} cadastrado com sucesso!")
            novo_id_cliente += 1

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
