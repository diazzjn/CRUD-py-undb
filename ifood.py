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

