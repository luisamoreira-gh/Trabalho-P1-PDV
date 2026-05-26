from datetime import datetime

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
    
def adiciona_carrinho(item, dic_itens, lista_itens, lista_preços, quantidade, lista_quantidade, lista_itens_relatorio, lista_qtde_relatorio):  #Função para adicionar itens no carrinho, remover itens do estoque e adicionar os preços à lista de preços
    if dic_itens[item]["Estoque"] >= quantidade:    #Checa a quantidade no estoque
        if item in lista_itens and dic_itens[item]["Estoque"] > 0:
            for i in range(quantidade):
                lista_preços.append(dic_itens[item]["Valor"])   #Loop para adicionar valores
            dic_itens[item]["Estoque"] -= quantidade
        elif item not in lista_itens and dic_itens[item]["Estoque"] > 0:
            lista_itens.append(item)   #Caso o item não esteja na lista de nomes (carrinho), adiciona
            lista_itens_relatorio.append(item)
            lista_quantidade.append(quantidade)
            lista_qtde_relatorio.append(quantidade)
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

def recibo(produtos, carrinho, preços_carrinho, nome_vendedor, carrinho_quantidade, vendedores, vendedores_relatorio):
    print("---------------------------------")
    print("      Recibo:")          
    for i in range(len(carrinho)):
        print(f"{carrinho[i]}: R${produtos[carrinho[i]]["Valor"]}0 x {carrinho_quantidade[i]}")
    soma_recibo = sum(preços_carrinho)
    soma_recibo_imposto = soma_recibo * 1.25
    somas.append(soma_recibo_imposto)
    valor_imposto = soma_recibo * 0.25
    valores_imposto.append(valor_imposto)
    print(f"VALOR DO IMPOSTO: R${valor_imposto}0")
    print(f"TOTAL: R${soma_recibo_imposto}0")
    data = datetime.now()
    data_brasil = data.strftime("%d/%m/%Y")
    print(data_brasil)
    print(f"VENDEDOR: {nome_vendedor.upper()}")
    print("---------------------------------")
    comissao = soma_recibo_imposto * 0.05
    vendedores[nome_vendedor.upper()]["Comissão"] += round(comissao,2 )
    vendedores_relatorio.append(nome_vendedor.upper())
    carrinho.clear()
    carrinho_quantidade.clear()
    preços_carrinho.clear()

def relatorio(relatorio_itens, somas, contador_vendas, valores_imposto, vendedores, vendedores_relatorio):
    print("---------------------------------")
    print("      Relatório:")
    print("Produtos vendidos:")
    for i in range(len(relatorio_itens)):
        print(relatorio_itens[i])
    total = sum(somas)
    print(f"VALOR TOTAL DAS VENDAS: R${total}0")
    print(f"QUANTIDADE TOTAL DE VENDAS: {contador_vendas}")
    total_imposto = sum(valores_imposto)   
    print(f"TOTAL DE IMPOSTO: R${total_imposto}0")  
    for i in range(len(vendedores_relatorio)):
        print(f"COMISSÃO {vendedores_relatorio[i]}: R${vendedores[vendedores_relatorio[i]]["Comissão"]}")
    print("---------------------------------")

contador_vendas = 0
relatorio_itens = []
relatorio_qtde = []
somas = []
carrinho = []
preços_carrinho = []
carrinho_quantidade = []
valores_imposto = []
vendedores_relatorio = []



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
            relatorio(relatorio_itens, somas, contador_vendas, valores_imposto, vendedores, vendedores_relatorio)
            break
        
        case 1:
            nome_item_novo = str(input("Qual produto você deseja adicionar?: ")).upper()
            preço_item_novo = float(input("Qual é o preço do novo produto?: "))
            estoque_item_novo = int(input("Quantos desse produto há no estoque?: "))
            adicionar_item(nome_item_novo, produtos, preço_item_novo, estoque_item_novo)
            print("Produto adicionado!")
  
        case 2:
            nome_novo_cliente = str(input("Qual é o nome do novo cliente?: ")).upper()
            adicionar_pessoa(nome_novo_cliente, clientes)
            print("Cliente adicionado!")
            
                
        case 3:
            nome_novo_vendedor = str(input("Qual é o nome do novo vendedor?: ")).upper()
            adicionar_pessoa(nome_novo_vendedor, vendedores)
            print("Vendedor adicionado!")
           
                
        case 4:
            while True:
                nome_cliente = str(input("Olá, cliente! Como você se chama?: "))
                if identificar_pessoa(nome_cliente, clientes) == False:
                    print("Desculpe, esse cliente não existe")
                    
                else:
                    break
            while True:
                nome_vendedor = str(input(f"Olá, {nome_cliente.upper()}! Como se chama o seu vendedor?: "))  
                if identificar_pessoa(nome_vendedor, vendedores) == False:
                    print("Desculpe, esse vendedor não existe")
                    
                else:
                    break
            while True:
                
                
                print("---------------------------------")
                print("      PRODUTOS DISPONÍVEIS:")
                for item in produtos:
                    print(item)
                print("---------------------------------")
                produto_desejado = input("Digite o nome do produto para adicionar ao carrinho, ou digite 'FINALIZAR' para terminar a compra: ").upper()

                if produto_desejado != "FINALIZAR":
                    if produto_desejado not in produtos:
                        print("Desculpe, esse produto não existe.")
                    else:
                        quantidade_desejada = int(input("Digite a quantidade de produtos desejada: "))
                        adiciona_carrinho(produto_desejado, produtos, carrinho, preços_carrinho, quantidade_desejada, carrinho_quantidade, relatorio_itens, relatorio_qtde)
                        
                                
                else:
                    recibo(produtos, carrinho, preços_carrinho, nome_vendedor, carrinho_quantidade, vendedores, vendedores_relatorio)
                    contador_vendas += 1
                    break
        case _:
            print("Desculpe, esse comando não existe. Tente novamente.")
            