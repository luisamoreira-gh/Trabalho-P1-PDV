produtos = {    #Cadastro de produtos – código, nome, valor, estoque
    "DETERGENTE" : {"Código" : 202601001, "Valor" : 3.99, "Estoque" : 16},
    "MIOJO" : {"Código" : 202601002, "Valor" : 3.50, "Estoque" : 21},    #O produto, identificado por seu nome, possui código, valor e estoque
    "GELADEIRA" : {"Código" : 202601003, "Valor" : 3899.00, "Estoque" : 3},
    "PAPEL" : {"Código" : 202601004, "Valor" : 45.00, "Estoque" : 14},
}

clientes = {    #Cadastro de clientes – código, nome
    "AMANDA" : {"Código" : 202602001},
    "BERNARDO" : {"Código" : 202602002},    #O cliente, identificado por seu nome, possui um código
    "CAROLINA" : {"Código" : 202602003},
    "DIOGO" : {"Código" : 202602004},
}

vendedores = {  #Cadastro de vendedores – código, nome
    "ANDERSON" : {"Código" : 202603001, "Comissão" : 0},
    "BEATRIZ" : {"Código" : 202603002, "Comissão" : 0},    #O vendedor, identificado por seu nome, possui um código e um valor de comissão
    "CARLOS" : {"Código" : 202603003, "Comissão" : 0},
    "DANIELA" : {"Código" : 202603004, "Comissão" : 0},
}

recomeçar = 1   #Loop para permitir a realização de mais compras por dia
while recomeçar == 1:
    carrinho = []   #Aqui ficarão os produtos selecionados até a conclusão da venda
    preços = [] #Aqui ficarão os valores dos produtos selecionados
    nome_cliente = str(input("Olá, caro cliente! Como você se chama?: "))
    while True:     #Toda compra deverá ser realizada por um cliente cadastrado e um vendedor
        existe_cliente = list(filter(lambda nome: nome == nome_cliente.upper(), clientes))
        if len(existe_cliente) == 0:     #O código cria uma lista com o nome do cliente, caso este esteja cadastrado. Caso contrário, pede novamente.
            print("Cliente não encontrado! Tente novamente.")
            nome_cliente = str(input("Olá, caro cliente! Como você se chama?: "))
        else:
            break   #O código para ao encontrar o cliente cadastrado
        
    nome_vendedor = str(input(f"Olá, {existe_cliente[0]}! Quem está te atendendo?: "))
    while True:
        vendedor_upper = nome_vendedor.upper()
        existe_vendedor = list(filter(lambda nome: nome == vendedor_upper, vendedores))
        if len(existe_vendedor) == 0:    #O código cria uma lista com o nome do vendedor, caso este esteja cadastrado. Caso contrário, pede novamente.
            print("Vendedor não encontrado! Tente novamente.")
            nome_vendedor = str(input(f"Olá, {existe_cliente[0]}! Quem está te atendendo?: "))
        else:
            vendedores[vendedor_upper]["Comissão"] += 1
            break   #O código para ao encontrar o vendedor cadastrado
    
    recomeçar = int(input("Compra finalizada! Para realizar uma nova compra, aperte 1. Para receber o relatório do dia, digite 0: "))
    while recomeçar > 1:   #Variável "recomeçar" retorna para definir o fim ou a continuação do código
        print("Número inválido! Tente novamente.")
        recomeçar = int(input("Compra finalizada! Para realizar uma nova compra, aperte 1. Para receber o relatório do dia, digite 0: "))
    if recomeçar == 0:  #Caso finalizado, exibirá o relatório do dia – Produtos vendidos, total de vendas, imposto, comissão por vendedor.
        break