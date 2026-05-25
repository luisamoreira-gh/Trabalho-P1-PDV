produtos = [   #CADASTRO DE PRODUTOS
    {"código": 20261001, "nome": "Vestido", "preço": 150.00, "estoque": 50},
    {"código": 20261002, "nome": "Calça", "preço": 120.00, "estoque": 30},
    {"código": 20261003, "nome": "Bolsa", "preço": 300.00, "estoque": 20},
]

clientes = [   #CADASTRO DE CLIENTES
    {"código": 20262001, "nome": "Bianca"},
    {"código": 20262002, "nome": "Ana"},
    {"código": 20262003, "nome": "Jade"},
]

vendedores = [   #CADASTRO DE VENDEDORES
    {"código": 20263001, "nome": "Beatriz", "comissão": 0},
    {"código": 20263002, "nome": "Ana Bruna", "comissão": 0},
    {"código": 20263003, "nome": "Gabriela", "comissão": 0},
    {"código": 20263004, "nome": "Luísa", "comissão": 0},
]

vendas = []  #Lista para armazenar as vendas realizadas

def linha(): #Função para melhorar a estética e organização so sistema
    print("-" * 30)
    
#FUNÇÕES DE CADASTRO    
    
def cadastrar_produto():
    print("===== Cadastro de Produto =====")
    nome = input("Digite o nome do produto: ")
    codigo = int(input("Digite o código do produto: "))
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite a quantidade em estoque: "))
    
    #Cria um dicionário para o novo produto e o adiciona à lista de produtos
    novo_produto = {"código": codigo, "nome": nome, "preço": preco, "estoque": estoque}
    produtos.append(novo_produto)
    print("Produto cadastrado com sucesso!")
    
def cadastrar_cliente():
    print("===== Cadastro de Cliente =====")
    nome = input("Digite o nome do cliente: ")
    codigo = int(input("Digite o código do cliente: "))
    
    #Cria um dicionário para o novo cliente e o adiciona à lista de clientes
    novo_cliente = {"código": codigo, "nome": nome}
    clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso!")
    
def cadastrar_vendedor():
    print("===== Cadastro de Vendedor =====")
    nome = input("Digite o nome do vendedor: ")
    codigo = int(input("Digite o código do vendedor: "))
    
    #Cria um dicionário para o novo vendedor e o adiciona à lista de vendedores
    #Todo vendedor inicia com comissão 0
    novo_vendedor = {"código": codigo, "nome": nome, "comissão": 0}
    vendedores.append(novo_vendedor)
    print("Vendedor cadastrado com sucesso!")
    
#FLUXO DE VENDA    
    
def nova_compra():
    #Validação do vendedor
    cod_vendedor = int(input("Digite o código do vendedor: "))
    vendedor = buscar_vendedor(cod_vendedor)
    if vendedor is None:
        print("Vendedor não encontrado! Operação cancelada.")
        return
    
    #Validação do cliente
    cod_cliente = int(input("Digite o código do cliente: "))
    cliente = buscar_cliente(cod_cliente)
    if cliente is None:
        print("Cliente não encontrado! Operação cancelada.")
        return
    
    data = input("Digite a data de hoje (ex: 21/05/2026): ")
    
    print(f"VEndedor: {vendedor['nome']} - Cliente: {cliente['nome']} - Data: {data}")
    
    #Lista para armazenar os itens da compra e o total da venda
    itens = []
    total = 0
    
    #Loop para adicionar produtos à compra
    while True:
        cod_produto = int(input("Digite o código do produto (0 para finalizar): "))
        if cod_produto == 0:
            break
        
        produto = buscar_produto(cod_produto)
        if produto is None:
            print("Produto não encontrado! Tente novamente.")
        else:
            qnt = int(input(f"Digite a quantidade de {produto['nome']} desejada: "))
           
        #Validação da quantidade em estoque
            if qnt > produto['estoque']:
                print(f"Quantidade indisponível! Estoque atual: {produto['estoque']}")
                continue
            
        #Atualiza o estoque do produto
            produto['estoque'] -= qnt
            subtotal = produto['preço'] * qnt
            total += subtotal
            
        #Adiciona o item à lista de itens da compra
            itens.append({
                "produto": produto['nome'], 
                "quantidade": qnt, 
                "subtotal": subtotal})
            linha()
            print(f"Produto {produto['nome']} adicionado ao carrimho. Subtotal: R${subtotal:.2f}")
            linha()
            
    #Cálculo do imposto
    if len(itens) > 0:
        imposto = total * 0.25
        comissao = total * 0.05
            
        #Atualiza a comissão do vendedor e registra a venda na lista de vendas
        vendedor['comissão'] += comissao
        venda_final = {
            "vendedor": vendedor['nome'],
            "cliente": cliente['nome'],
            "itens": itens,
            "total": total,
            "imposto": imposto,
            "comissão": comissao,
            "data": data
        }
        vendas.append(venda_final)
            
        #Exibe o recibo da venda
        print("===== RECIBO DA VENDA =====")
        print(f"VENDEDOR:{vendedor['nome']}")
        print(f"CLIENTE: {cliente['nome']}")
        print(f"DATA: {data}")
        linha()
        print("ITENS:")
        for item in itens:
            print(f"{item['produto']} - Quantidade: {item['quantidade']} - Subtotal: R${item['subtotal']:.2f}")
        linha()
        print(f"TOTAL: R${total:.2f}")
    else:
        print("Nenhum item adicionado. Compra cancelada.")
        
        
def relatorio_vendas():
    print("===== RELATÓRIO GERAL DE VENDAS =====")
    if len(vendas) == 0:
        print("Nenhuma venda foi realizada hoje.")
        return
   
   #Variáveis para acumular o faturamento total e o imposto total
    faturamento_total = 0
    imposto_total = 0
    
    linha()
    print("   HISTÓRICO   ")
    linha()
    
    #Exibe o histórico detalhado de vendas, incluindo vendedor, cliente, data, itens vendidos, total, imposto e comissão
    for v in vendas:
        print(f"VENDEDOR: {v['vendedor']} - CLIENTE: {v['cliente']} - DATA: {v['data']}")
        
        print("ITENS:")
        for item in v['itens']:
            print(f"{item['produto']} - Quantidade: {item['quantidade']} - Subtotal: R${item['subtotal']:.2f}")
        print(f"TOTAL: R${v['total']:.2f} - IMPOSTO: R${v['imposto']:.2f} - COMISSÃO: R${v['comissão']:.2f}")
        linha()
        
        #Atualiza o faturamento total e o imposto total com os valores da venda atual
        faturamento_total += v['total']
        imposto_total += v['imposto']
    
    print("   RESUMO FINANCEIRO:   ")
    linha()
    print(f"TOTAL DE VENDAS (Faturamento Bruto): R${faturamento_total:.2f}")
    print(f"TOTAL DE IMPOSTOS(25%):  R${imposto_total:.2f}")
    
    linha()
    print("   COMISSÃO POR VENDEDOR:   ")
    linha()
    
    #Exibe a comisão acumulada de cada vendedor
    for vender in vendedores:
        print(f"Vendedor: {vender['nome']} - Comissão Acumulada: R${vender['comissão']:.2f}")
        
#FUNÇÕES DE BUSCA
    
def buscar_cliente(codigo):
    for cliente in clientes:
        if cliente["código"] == codigo:
            return cliente #Retorna o cliente encontrado (DICIONÁRIO) ou None se não encontrado
    return None
    
def buscar_vendedor(codigo):
    for vendedor in vendedores:
        if vendedor["código"] == codigo:
            return vendedor #Retorna o vendedor encontrado (DICIONÁRIO) ou None se não encontrado
    return None

def buscar_produto(codigo):
    for produto in produtos:
        if produto["código"] == codigo:
            return produto #Retorna o produto encontrado (DICIONÁRIO) ou None se não encontrado
    return None
    
#FLUXO PRINCIPAL DO SISTEMA - EXIBIÇÃO DO MENU E CHAMADA DAS FUNÇÕES DE ACORDO COM A OPÇÃO ESCOLHIDA PELO USUÁRIO
    
while True:
    print('''

    =========================================
            SISTEMA PDV - DEMETRIUS        
    =========================================
    1. Cadastrar Produto
    2. Cadastrar Cliente
    3. Cadastrar Vendedor
    4. Realizar Nova Compra
    5. Exibir Relatório de Vendas
    0. Sair do Sistema
    =========================================
    ''')
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 0:
        print("Saindo do sistema. Até logo!")
        break
    elif opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        cadastrar_cliente()
    elif opcao == 3:
        cadastrar_vendedor()
    elif opcao == 4:
        nova_compra()
    elif opcao == 5:
        relatorio_vendas()