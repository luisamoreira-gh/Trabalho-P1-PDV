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
        
def adicionar_pessoa(nome_recebido, dic_pessoa):
    ultimo_item = list(dic_pessoa.values())[-1]
    ultimo_codigo = ultimo_item["Código"]
    if dic_pessoa == vendedores:
        dic_pessoa.update({nome_recebido.upper(): {"Código" : ultimo_codigo + 1, "Comissão" : 0}})
        return dic_pessoa
    elif dic_pessoa == clientes:
        dic_pessoa.update({nome_recebido.upper(): {"Código" : ultimo_codigo +1}})
        return dic_pessoa
    
def adicionar_item(item, dic_itens, valor, quantidade):
    ultimo_item = list(dic_itens.values())[-1]
    ultimo_codigo = ultimo_item["Código"]
    dic_itens.update({item.upper(): {"Código" : ultimo_codigo +1, "Valor" : valor, "Estoque" : quantidade}})
    return dic_itens

produtos_vendidos = {
    "DETERGENTE" : {"Quantidade" : 0},
    "MIOJO" : {"Quantidade" : 0},
    "GELADEIRA" : {"Quantidade" : 0},
    "PAPEL" : {"Quantidade" : 0},
    }
valor_total = []
valor_imposto = []

while True:
    print("--------------------------------------------")
    print("  Digite 1 para cadastrar um novo produto")
    print("  Digite 2 para cadastrar um novo cliente")
    print("  Digite 3 para cadastrar um novo vendedor")
    print("  Digite 4 para iniciar uma compra")
    print("  Digite 0 para exibir o relatório diário")
    print("--------------------------------------------")
    comando_inicial = int(input("Digite aqui seu comando: "))
    match comando_inicial:
        case 0:
            print("")
            break
        
        case 1:
            nome_item_novo = str(input("Qual produto você deseja adicionar?: ")).upper()
            preço_item_novo = float(input("Qual é o preço do novo produto?: "))
            estoque_item_novo = int(input("Quantos desse produto há no estoque?: "))
            adicionar_item(nome_item_novo, produtos, preço_item_novo, estoque_item_novo)
            print("Produto adicionado!")
            continue
                
        case 2:
            nome_novo_cliente = str(input("Qual é o nome do novo cliente?: ")).upper()
            adicionar_pessoa(nome_novo_cliente, clientes)
            print("Cliente adicionado!")
            continue
                
        case 3:
            nome_novo_vendedor = str(input("Qual é o nome do novo vendedor?: ")).upper()
            adicionar_pessoa(nome_novo_vendedor, vendedores)
            print("Vendedor adicionado!")
            continue
                
        case 4:
            while True:
                nome_cliente = str(input("Olá, cliente! Como você se chama?: "))
                if identificar_pessoa(nome_cliente, clientes) == False:
                    print("Desculpe, esse cliente não existe")
                    continue
                else:
                    break
            while True:
                nome_vendedor = str(input(f"Olá, {nome_cliente.upper()}! Como se chama o seu vendedor?: "))  
                if identificar_pessoa(nome_vendedor, vendedores) == False:
                    print("Desculpe, esse vendedor não existe")
                    continue
                else:
                    break
            while True:
                carrinho = []
                preços_carrinho = []
                print("---------------------------------")
                print("      PRODUTOS DISPONÍVEIS:")
                for item in produtos:
                    print(item)
                print("---------------------------------")
                produto_desejado = str(input("Digite o nome do produto para adicionar ao carrinho, ou digite 'FINALIZAR' para terminar a compra: ")).upper()
                produtos_vendidos.update(produto_desejado)
                if produto_desejado != "FINALIZAR":
                    if produto_desejado not in produtos:
                        print("Desculpe, esse produto não existe.")
                    else:
                        quantidade_desejada = int(input("Digite a quantidade de produtos desejada: "))
                        adiciona_carrinho(produto_desejado, produtos, carrinho, preços_carrinho, quantidade_desejada)
                        
                else:
                    break
        case _:
            print("Desculpe, esse comando não existe. Tente novamente.")
            continue