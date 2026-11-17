# CRUD-py-undb
- Introdução
O projeto consiste no desenvolvimento de um sistema simples de delivery inspirado no funcionamento do iFood, utilizando a linguagem Python. O objetivo é simular o gerenciamento de clientes, restaurantes, entregadores e pedidos por meio de um menu interativo no terminal.

- Objetivo do sistema
O sistema tem como objetivo permitir o cadastro, a consulta, a atualização e a exclusão de informações, além de possibilitar a criação de pedidos a partir dos cardápios dos restaurantes cadastrados.

- Tecnologias e conteúdos utilizados
O projeto foi desenvolvido utilizando Python e conceitos básicos de lógica de programação:
 Variáveis: armazenam informações e controlam os IDs dos registros.
 Listas: armazenam clientes, restaurantes, entregadores e pedidos.
 Dicionários: organizam os dados de cada registro, como nome, endereço, telefone e ID.
 Condicionais (if, elif e else): verificam opções escolhidas e condições do sistema.
 Laços while: mantêm os menus em funcionamento até que o usuário escolha sair.
 Laços for: percorrem as listas para localizar e apresentar informações.
 Entrada de dados (input): recebe informações digitadas pelo usuário.
 Saída de dados (print): apresenta menus, mensagens e resultados no terminal.

- Funcionalidades do sistema
  Área	Funcionalidades
Clientes	Cadastrar, listar, consultar, atualizar e excluir clientes.
Restaurantes	Cadastrar, listar, consultar, atualizar e excluir restaurantes.
Entregadores	Cadastrar, listar, consultar, atualizar e excluir entregadores.
Pedidos	Criar, listar, consultar, atualizar status e excluir pedidos.

- Funcionamento do sistema
Ao iniciar o programa, o usuário encontra um menu principal com as opções de clientes, restaurantes, entregadores, pedidos e saída.
Cada opção possui um submenu com as operações disponíveis. O usuário escolhe uma opção digitando o número correspondente.
Para realizar um pedido, o sistema solicita os IDs do cliente, restaurante e entregador. Em seguida, apresenta o cardápio do restaurante escolhido, permitindo selecionar os produtos desejados e calcular automaticamente o valor total.
Cada pedido recebe um ID próprio e inicia com o status "Preparando", que pode ser atualizado posteriormente para "Saiu para entrega", "Entregue" ou "Cancelado".

- Organização dos dados
ex
clientes.append({
    "id": 1,
    "nome": "João",
    "endereco": "Rua A, 1234",
    "telefone": "9898756909"
})
Nesse exemplo, a lista clientes armazena um dicionário com as informações de um cliente. Os pedidos utilizam os IDs para relacionar clientes, restaurantes e entregadores, permitindo identificar a quem cada pedido pertence.

- Regras de funcionamento
O sistema possui algumas regras para evitar problemas durante sua utilização:
 Não permite excluir clientes que possuem pedidos cadastrados.
 Não permite excluir restaurantes que possuem pedidos cadastrados.
 Não permite excluir entregadores que estão associados a pedidos.
 Não permite criar pedidos sem selecionar itens do cardápio.
 Verifica se os IDs informados existem antes de realizar determinadas operações.
 Permite manter informações antigas durante uma atualização pressionando Enter.
 Verifica se o número escolhido no cardápio corresponde a um prato existente.

- O desenvolvimento desse projeto permitiu aplicar conhecimentos de lógica de programação e Python na construção de um sistema com diferentes funcionalidades. Durante sua implementação, foram utilizados conceitos como listas, dicionários, variáveis, condicionais e estruturas de repetição.
O projeto também contribuiu para compreender como organizar informações, realizar operações CRUD e relacionar diferentes dados utilizando IDs. Dessa forma, foi possível desenvolver uma aplicação prática para exercitar os conteúdos estudados na disciplina.
Observação: Esta documentação descreve o funcionamento do código enviado. Os dados são armazenados em memória, portanto, ao encerrar o programa, os cadastros realizados durante a execução não ficam salvos permanentemente.
