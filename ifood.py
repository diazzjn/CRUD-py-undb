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
    print("5.voltar")
    opcao = input("escolha uma opção: ")

    if opcao == "1":
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
            print("Cliente {nome} cadastrado com sucesso!")
            novo_id_cliente += 1
