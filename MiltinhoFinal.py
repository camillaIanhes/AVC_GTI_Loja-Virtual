
msg_menu = "Continue navegando em nosso menu "
msg_inicio_menu = "Bem vindo a nossa loja "
nome_cliente = ""

## Váriaveis para controle de valor total e desconto do pedido ----------
valor_total_pedido = 0.0
percentual_desconto = 0.1 ## 10%
valor_minimo_desconto = 200
## ----------------------------------------------------------------------

lista_de_produtos_cliente = []
base_de_encomendas = {}
base_de_produtos = [
    ("teclado", "Eletrônico", 100.00, 10),
    ("camiseta", "Roupa", 50.00, 20),
    ("calça", "Roupa", 100.00, 10),
    ("tenis", "Calçado", 300.00, 30)
]

while True:
    if not nome_cliente:
        msg_inicio_menu = "Bem vindo a nossa loja "
        nome_cliente = input("Para fazer um pedido, informe seu nome: ")
        print("")
        if not nome_cliente :       
            print(
            "------------------------------------------------------ ")
            print(
            "- Nome nao pode ser vazio ---------------------------- ")
            print(
            "------------------------------------------------------ ")
    else:
        opcao_menu = input(
            msg_inicio_menu + nome_cliente + "!! \n" +
            "-------------------------- MENU ---------------------- \n" +
            "[1] Listar Produtos Disponiveis ---------------------- \n" +
            "[2] Fazer um pedido ---------------------------------- \n" +
            "[3] Visualizar pedido  ------------------------------- \n" +
            "[4] Deletar produtos de um pedido  ------------------- \n" +
            "[5] Finalizar Pedido --------------------------------- \n" +
            "[6] Cadastrar novos produtos na loja ----------------- \n" +
            "[7] Sair --------------------------------------------- \n"             
        )
        ## Listar os produtos disponiveis na base de produtos da loja
        # base_de_produtos
        if opcao_menu == "1":
            print("- Produtos disponivéis: ")
            for p in base_de_produtos:
                print(f"| {p[0]} - categoria: {p[1]}, preço: {p[2]}, estoque: {p[3]}")
            print("")
            msg_inicio_menu = msg_menu

        ## Criar um pedido e fazer um loop para adicionar quantos produtos o cliente quiser, já validando o estoque 
        #  disponivel e calculando o valor total do pedido.
        elif opcao_menu == "2":
            adicionar_produto = True ## Usando essa variável para controle do loop, manter true até o cliente não quiser mais adicionar produtos
            while adicionar_produto:
                nome_produto = input("- Nome do produto: ").lower()
                achou_prod = False ## Variável de controle para definir o fluxo caso o cliente digite um produto que não exista na base.
                base_produtos_atualizada = []
                for p in base_de_produtos:
                    if p[0] == nome_produto:
                        qtd_prod = int(input("- Quantidade de produtos: ")) ## variável para o cliente informar a quantidade de produtos
                        achou_prod = True
                        if qtd_prod > p[3]:  ## Aqui começa o controle de estoque - Validando se tem estoque para a quantidade do cliente
                            print("")
                            print("- O pedido ultrapassa o nosso estoque :/ ")
                            print("")
                            break
                        ## calculo para saber o valor total do pedido 
                        # Aqui usamos o operador de atribuição += para iterar a base de produtos e somar os valores de cada produto do cliente 
                        valor_total_pedido += (qtd_prod * p[2])  ## Se não usar o operado de atribuição ficaria assim: valor_total_pedido = valor_total_pedido + (qtd_prod * p[2])             
                        
                        produto_pedido = (p[0], p[2], qtd_prod) ## Aqui definimos como será a tupla para identificar um pedido                
                        
                        lista_de_produtos_cliente.append(produto_pedido)
                        
                        ## Aqui criamos a base de pedidos de um cliente, usando um dicionário com a lista de produtos e o valot total
                        base_de_encomendas[nome_cliente] = {
                            "produtos": lista_de_produtos_cliente,
                            "valor_total": valor_total_pedido
                        }
                        ## Atualizando estoque com base na quantidade e produtos do pedido
                        # Para atualizar o estoque precisamos criar uma nova lista de produtos da loja atualizada que vamso iterar 
                        # e atribuir o produto já com o calculo atualizado do estoque
                        estoque_atualizado = p[3] - qtd_prod
                        base_produtos_atualizada.append((p[0], p[1], p[2], estoque_atualizado))
                    else:
                        ## Como estamos criando uma nova lista atualizada, para cada produto que não seja o escolhido do cliente
                        #  precisamos adicionar nela sem alterar nada
                        base_produtos_atualizada.append((p[0], p[1], p[2], p[3])) 
                if base_produtos_atualizada:
                    ## A base atualizada estando preenchida então vamsoa tualizar a base principal com os valores da base atualizada
                    # dessa forma podemos continuar usando a base de produtos em outros momentos.
                    base_de_produtos = base_produtos_atualizada

                if not achou_prod:
                    print("- O produto mencionado não foi encontrado :(")
                    print(" ")
                    msg_inicio_menu = msg_menu
                    break
                continuar_adicionando = input("- Adicionar mais produtos: \n" +
                                            "[1] Sim \n" +
                                            "[2] Nao \n")      
                if continuar_adicionando != "1":
                    adicionar_produto = False
                    print(" ")
                    msg_inicio_menu = msg_menu

        ## Mostrar informações do pedio
        elif opcao_menu == "3":
            if nome_cliente in base_de_encomendas:
                print("Segue seu pedido: ")
                pedido = base_de_encomendas[nome_cliente]
                
                ## precisa lembrar que sempre deve definir qual item do dicionário queremos usar
                # o dicionário de pedidos tem a lista de produtos e também o valor total, então quando queremos saber dos produtos, precisamos 
                # definir a chave "produtos"
                for p in pedido["produtos"]: 
                    print(f"| {p[0]} - preço: {p[1]}, quantidade: {p[2]}")
                valor_pedido = pedido["valor_total"]
                print(f"- Total do pedido: {valor_pedido}")
                print("")
            else:
                print("- Você não tem pedidos ainda")
                print("")
                msg_inicio_menu = msg_menu

        elif opcao_menu == "4":
            if not lista_de_produtos_cliente :
                print("- Você não tem um pedido")
                print("")
            else:
                lista_de_produtos_atualizada = lista_de_produtos_cliente
                nome_produto_remover = input("Nome do produto: ").lower()
                achou_prod = False
                ## Aqui seguimos a mesma estratégia do menu 2 - Fazer um pedido para atualizar o estoque e o valor total do pedido
                for produto in lista_de_produtos_cliente:
                    if produto[0] == nome_produto_remover:
                        achou_prod = True
                        lista_de_produtos_atualizada.remove(produto)
                        base_de_encomendas[nome_cliente]["produtos"] = lista_de_produtos_atualizada

                        ## Atualiza o valor total do pedido considerando o produto que foi removido
                        valor_total_pedido -= (produto[2] * produto[1])
                        base_de_encomendas[nome_cliente]["valor_total"] = valor_total_pedido

                        ## Atualizando estoque da base de produtos da loja depois de remover o item do pedido                   
                        base_produtos_atualizada = []
                        for p_base in base_de_produtos:
                            if p_base[0] == nome_produto_remover:
                                estoque_atualizado = p_base[3] + produto[2]
                                base_produtos_atualizada.append((p_base[0], p_base[1], p_base[2], estoque_atualizado))
                            else:
                                base_produtos_atualizada.append((p_base[0], p_base[1], p_base[2], p_base[3]))
                        base_de_produtos = base_produtos_atualizada

                if achou_prod :
                    ## Se o cliente tirar todos os produtos de um pedido, o pedido deixa de existir
                    if not base_de_encomendas[nome_cliente]["produtos"]:
                        del base_de_encomendas[nome_cliente]
                        valor_total_pedido = 0.0
                        print("- Voce deletou todos os itens do pedido! ")
                        print("")
                    else:
                        print("")
                        print("- Pedido atualizado! ")
                        print("")
                        pedido = base_de_encomendas[nome_cliente]
                        for p in pedido["produtos"]:
                            print(f"| {p[0]} - preço: {p[1]}, quantidade: {p[2]}")
                        valor_pedido = pedido["valor_total"]
                        print(f"- Total do pedido: {valor_pedido}")
                        print("")
                else:
                    print("")
                    print("- O produto mencionado não foi encontrado! ")
                    print("")
            msg_inicio_menu = msg_menu

        ## Finalizar o pedido, aqui vamos calcular se o cliente tem direito a um desconto e quanto de desconto foi aplicado. 
        # Quando o pedido é finalizado zeramos o dicionário de pedidos para que seja possivel um mesmo cliente fazer um novo pedido
        elif opcao_menu == "5":    
            if nome_cliente in base_de_encomendas :
                print(" ")
                print("Seguem os detalhes do pedido: ")
                pedido = base_de_encomendas[nome_cliente]
                for p in pedido["produtos"]:
                    print(f"| {p[0]} - preço: {p[1]}, quantidade: {p[2]}")
                valor_pedido = pedido["valor_total"]
                print(f"- Total do pedido: {valor_pedido}")
                print("")
                confirmacao_pedido = input("- Confirme se o seu pedido está correto: \n" +
                                            "[1] Sim, quero finalizar \n" +
                                            "[2] Nao, voltar ao menu \n")
                if confirmacao_pedido == "1":
                    valor_pedido = pedido["valor_total"]       
                    if valor_pedido > valor_minimo_desconto:
                        valor_desconto = valor_pedido * percentual_desconto  
                        valor_pedido_desconto = valor_pedido - valor_desconto
                        print("##  PARABÉNS  ##")
                        print(f"## Você ganhou um desconto no valor de [ {valor_desconto} reais ] ##")
                        print(f"- Total do pedido com desconto: {valor_pedido_desconto}")

                    del base_de_encomendas[nome_cliente]
                    lista_de_produtos_cliente = [] 
                    valor_total_pedido = 0.0
                    print("")
                    print("## Seu pedido foi finalizado com sucesso ##")
                    print("## Obrigado por comprar com a gente!!    ##")
                    print("")
            else:
                print("- Você não tem pedidos ainda")
                print("")
                msg_inicio_menu = msg_menu
#nessa parte vamos criar um nome produto, então usamos operadores boleanos e nesse caso precisamos que seja FALSE
#para ele adicionar um novo produto.
        elif opcao_menu == "6": 
            print("- Informe os dados do produto para cadastro: ")
            nome_produto = input("| Nome do produto: ").lower() #lower usamos para não dar erro se o usuario escrever
            produto_existe = False                               # em letra maiuscula ou minuscula
            for produto in base_de_produtos:
                if produto[0] == nome_produto:
                    produto_existe = True
                    break
            if produto_existe: #se o comando acima for true, ele dá a resposta que ja existe esse produto
                print("")
                print("- Esse produto já existe em nossa loja ")
                print("")
            else: #se o comando acima for false, vai pedir passo a passo para o usuario cadastrar um novo
                categoria_produto = input("| Categoria do produto: ")
                preco_produto = float(input("| Preço do produto: "))
                qtd_estoque = int(input("| Quantidade do estoque: "))
                
                novo_produto = (nome_produto, categoria_produto, preco_produto, qtd_estoque)
                #mostra aqui que foi adcionado na base_de_produtos o nome pedido cadastrado
                base_de_produtos.append(novo_produto)
                print("") #append serve somente para adicionar em lista, nao serve para dicionario e tuplas!!
                print("- Produto adicionado com sucesso ")
                print(f"| {nome_produto} - categoria: {categoria_produto}, preço: {preco_produto}, estoque: {qtd_estoque}")
                print("")
            msg_inicio_menu = msg_menu

        elif opcao_menu == "7":
            ## Essa opção permite a troca clientes no menu da loja, quando um cliente sai a nós zeramos a lista em memória e o total 
            # mantendo somente o dicionário de pedido do cliente, dessa forma é possivel que um novo cliente crie um novo pedido no menu da loja
            print(f"## Volte sempre {nome_cliente}")
            print("")
            nome_cliente = "" 
            lista_de_produtos_cliente = [] 
            valor_total_pedido = 0.0       
        else:
            print("")
            print("- Por favor, escolha uma opção válida do Menu")
            print("")
            msg_inicio_menu = msg_menu