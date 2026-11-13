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
    print("\nBem-vindo ao iFood!")
    print("1.clientes")
    print("2.restaurantes")
    print("3.entregadores")
    print("4.pedidos")
    print("5.sair")
    opcao = input("escolha uma opção: ")

    if opcao == "1":
        print("\n--- CLIENTES ---")
        print("1.cadastrar clientes")
        print("2.listar clientes")
        print("3.consultar por id")
        print("4.atualizar")
        print("5.apagar")
        print("6.voltar")
        op = input("escolha uma opção: ")

    if opcao == "1":
        nome = input("digite o nome do cliente: ")
        endereco = input("digite o endereço do cliente: ")
        telefone = input("digite o telefone do cliente: ")
        clientes.append({"id": novo_id_cliente, "nome": nome, "endereco": endereco, "telefone": telefone})
        print(f"Cliente {nome} cadastrado com sucesso!")
        novo_id_cliente += 1

    elif op == "2":
        if len(clientes) == 0:
                print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(f"ID: {cliente['id']}")
                print(f"Nome: {cliente['nome']}")
                print(f"Endereço: {cliente['endereco']}")
                print(f"Telefone: {cliente['telefone']}")

    elif op == "3":
         id_consulta = int(input("Digite o ID do cliente que deseja consultar: "))
         achou = False
    for cliente in clientes:
        if clientes["id"] == id_consulta:
            if str(cliente["id"]) == str(id_consulta):
                print(f"Nome:", cliente["nome"])
                print(f"Endereço:", cliente["endereco"])
                print(f"Telefone:", cliente["telefone"])
                achou = True
        if achou == False:
            print("Cliente não encontrado.")
