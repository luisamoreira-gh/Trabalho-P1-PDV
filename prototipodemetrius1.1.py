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

def identificar_pessoa(nome_recebido, dicionario):  #Função para localizar o usuário, seja cliente ou vendedor.
    nome_upper = nome_recebido.upper()
    if nome_upper in dicionario:    #Compara o nome recebido com os nomes da lista de clientes/vendedores
        return True
    else: 
        return False
    
def adiciona_carrinho(item, dic_itens, lista_itens, lista_preços, quantidade):  #Função para adicionar itens no carrinho, remover itens do estoque e adicionar os preços à lista de preços
    if dic_itens[item]["Estoque"] >= quantidade:    #Checa a quantidade no estoque
        if item in lista_itens and dic_itens[item]["Estoque"] > 0:
            for i in range(quantidade):
                lista_preços.append(dic_itens[item]["Valor"])   #Loop para adicionar valores
            dic_itens[item]["Estoque"] -= quantidade
        elif item not in lista_itens and dic_itens[item]["Estoque"] > 0:
            lista_itens.append(item)    #Caso o item não esteja na lista de nomes (carrinho), adiciona
            for i in range(quantidade):
                lista_preços.append(dic_itens[item]["Valor"])
            dic_itens[item]["Estoque"] -= quantidade    #Remove itens do estoque
    else:
        print(f"Desculpe, só temos {dic_itens[item]["Estoque"]} desse item no estoque!")

while True:     #Loop principal
    carrinho = []
    preços = []
    nome_cliente = str(input("Olá, cliente! Como você se chama?: "))
    if identificar_pessoa(nome_cliente, clientes) == False:
        print("Desculpe, esse cliente não existe")
        continue
    else:
        breakpoint  #Para o sistema ao encontrar o cliente
    
    while True:
        nome_vendedor = str(input(f"Olá, {nome_cliente.upper()}! Como se chama o seu vendedor?: "))  
        if identificar_pessoa(nome_vendedor, vendedores) == False:
            print("Desculpe, esse vendedor não existe")
            continue
        else:
            vendedores[nome_vendedor.upper()]["Comissão"] += 1  #Adiciona +1 à comissão de vendas
            break   #Para o sistema ao encontrar o vendedor
    
    while True:
        print("---------------------------------")
        print("      PRODUTOS DISPONÍVEIS:")
        print("	   Detergente")
        print("	     Miojo")
        print("	   Geladeira")
        print("	     Papel")
        print("---------------------------------")
        produto_desejado = str(input("Digite o nome do produto para adicionar ao carrinho, ou digite 'FINALIZAR' para terminar a compra: "))
        if produto_desejado.upper() != "FINALIZAR":
            if produto_desejado.upper() not in produtos:
                print("Desculpe, esse produto não existe.")
            else:
                quantidade_desejada = int(input("Digite a quantidade de produtos desejada: "))
                adiciona_carrinho(produto_desejado.upper(), produtos, carrinho, preços, quantidade_desejada)
                continue
        else:
            print()
            break
    
    recomeçar = int(input("Compra finalizada! Para realizar uma nova compra, aperte 1. Para receber o relatório do dia, digite 0: "))
    while recomeçar > 1:
        print("Número inválido! Tente novamente.")
        recomeçar = int(input("Compra finalizada! Para realizar uma nova compra, aperte 1. Para receber o relatório do dia, digite 0: "))
    if recomeçar == 0:
        print("")
        break