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

restaurantes.append({"id": 1, "nome": "Pizzaria", "endereco": "Rua B, 5678",
                     "cardapio": cardapio_pizzaria})
restaurantes.append({"id": 2, "nome": "Hamburgueria", "endereco": "Av. C, 100",
                     "cardapio": cardapio_hamburgueria})
restaurantes.append({"id": 3, "nome": "Churrascaria", "endereco": "Rua D, 200",
                     "cardapio": cardapio_churrascaria})

entregadores.append({"id": 1, "nome": "Maria", "veiculo": "Moto"})


novo_id_cliente = 2
novo_id_restaurante = 4
novo_id_entregador = 2
novo_id_pedido = 1

while True:
    print("\n ---BEM-VINDO AO IFOOD---")
    print("1 - Clientes")
    print("2 - Restaurantes")
    print("3 - Entregadores")
    print("4 - Pedidos")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")