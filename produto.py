produto = [
    {
        "codigo": "001",
        "nome": "vestido",
        "valor": 100.0,
        "estoque": 10
    },
    {
        "codigo": "002",
        "nome": "calça",
        "valor": 150.0,
        "estoque": 5
    },
    {
        "codigo": "003",
        "nome": "camisa",
        "valor": 80.0,
        "estoque": 20
    }
]

clientes = [
    {
        "codigo": "001",
        "nome": "Lara",
        
    },
    {
        "codigo": "002",
        "nome": "Leticia",
        
    },
    {
        "codigo": "003",
        "nome": "Lena",
       
    }
]

vendedores = [
    {
        "codigo": "001",
        "nome": "Carol",
        "comissao": 0.5,
    },
    {
        "codigo": "002",
        "nome": "Salu",
        "comissao": 0.5,

    },
    {
        "codigo": "003",
        "nome": "Alice",
        "comissao": 0.5,
    }
]

vendas = []


def buscar_produto(codigo):
    for item in produto:
        if item["codigo"] == codigo:
            return item
    return None


def buscar_cliente(codigo):
    for cliente in clientes:
        if cliente["codigo"] == codigo:
            return cliente
    return None


def buscar_vendedor(codigo):
    for vendedor in vendedores:
        if vendedor["codigo"] == codigo:
            return vendedor
    return None


def realizar_venda():

    codigo_cliente = input("Digite o código do cliente: ")
    cliente = buscar_cliente(codigo_cliente)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    codigo_vendedor = input("Digite o código do vendedor: ")
    vendedor = buscar_vendedor(codigo_vendedor)

    if vendedor is None:
        print("Vendedor não encontrado.")
        return

    carrinho = []
    total = 0.0

    while True:

        codigo_produto = input(
            "Digite o código do produto (ou 'sair' para finalizar): "
        )

        if codigo_produto.lower() == "sair":
            break

        produto_encontrado = buscar_produto(codigo_produto)

        if produto_encontrado is None:
            print("Produto não encontrado.")
            continue

        quantidade = int(input("Digite a quantidade: "))

        if quantidade > produto_encontrado["estoque"]:
            print("Quantidade em estoque insuficiente.")
            continue

        subtotal = produto_encontrado["valor"] * quantidade

        item = {
            "produto": produto_encontrado["nome"],
            "quantidade": quantidade,
            "valor_unitario": produto_encontrado["valor"],
            "subtotal": subtotal,
            "comissao": subtotal * vendedores["comissao"]
        }

        carrinho.append(item)

        total += subtotal

        produto_encontrado["estoque"] -= quantidade

        print("Produto adicionado ao carrinho.")

    if not carrinho:
        print("Nenhum produto adicionado ao carrinho.")
        return

    continuar = input("Deseja finalizar a venda? (s/n): ")

    if continuar.lower() != "s":
        print("Venda cancelada.")
        return

    taxa_imposto = 0.25

    total_com_imposto = total * (1 + taxa_imposto)

    venda = {
        "cliente": cliente["nome"],
        "vendedor": vendedor["nome"],
        "itens": carrinho,
        "comissao_total": sum(item["comissao"] for item in carrinho),
        "total": total,
        "total_com_imposto": total_com_imposto
    }

    vendas.append(venda)

    print("\nVenda realizada com sucesso!")
    print(f"Cliente: {cliente['nome']}")
    print(f"Vendedor: {vendedor['nome']}")  
    print(f"item vendido: {carrinho}")
    print(f"Total da venda: R$ {total:.2f}")
    print(f"Comissão total: R$ {venda['comissao_total']:.2f}")
    print(f"Total com imposto: R$ {total_com_imposto:.2f}")
    



realizar_venda()
buscar_produto()
buscar_cliente()
buscar_vendedor()   