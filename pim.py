
# listas para armazenar dados
nomes = []
planos = []
mensalidades = []

valor_ingresso = 120


# função para linha bonita
def linha():
    print("-" * 45)


# função para mostrar menu
def menu():
    linha()
    print(" SISTEMA DE SÓCIO TORCEDOR CURINTIA ")
    linha()
    print("1 - Cadastrar Sócio")
    print("2 - Simular Venda de Ingresso")
    print("3 - Mostrar Sócios")
    print("0 - Sair")
    linha()


# função cadastro
def cadastrar():
    print("CADASTRO DE SÓCIO")

    nome = input("Nome do torcedor: ")

    print("Planos disponíveis:")
    print("OURO")
    print("PRATA")
    print("BRONZE")
    print("SOCIAL")

    plano = input("Digite o plano: ").upper()
    if plano != "OURO" and plano != "PRATA" and plano != "BRONZE" and plano != "SOCIAL":
        print("Plano inválido.")
        return

    pagamento = input("Mensalidade está paga? (S/N): ").upper()
    if pagamento == "S":
        mensalidade = True
    else:
        mensalidade = False

    # adicionando nas listas
    nomes.append(nome)
    planos.append(plano)
    mensalidades.append(mensalidade)
    print("Sócio cadastrado com sucesso!")


# função desconto
def calcular_desconto(plano):
    desconto = 0
    if plano == "OURO":
        desconto = 100
    elif plano == "SOCIAL":
        desconto = 80
    elif plano == "PRATA":
        desconto = 50
    elif plano == "BRONZE":
        desconto = 20
    else:
        desconto = 0
    return desconto


# função para calcular taxa extra
def taxa_servico(valor):
    taxa = valor * 0.05
    return taxa


# função ticket
def mostrar_ticket(nome, plano, valor_final):
    linha()
    print("TICKET DE COMPRA")
    linha()

    print("Nome:", nome)
    print("Plano:", plano)
    print("Valor final: R$", round(valor_final, 2))
    linha()


# venda de ingresso
def vender_ingresso():

    if len(nomes) == 0:
        print("Nenhum sócio cadastrado.")
        return

    print("LISTA DE SÓCIOS")
    for i in range(len(nomes)):
        print(i, "-", nomes[i])
    try:
        indice = int(input("Escolha o número do sócio: "))
    except:
        print("Valor inválido.")
        return





    if indice < 0:
        print("Número inválido.")
        return

    if indice >= len(nomes):
        print("Número inválido.")
        return
    nome = nomes[indice]
    plano = planos[indice]
    status = mensalidades[indice]

    # validação acesso
    if status == False:
        print("ACESSO NEGADO")
        print("Mensalidade em atraso.")
        return

    desconto = calcular_desconto(plano)
    valor = valor_ingresso
    valor_desconto = valor * (desconto / 100)
    valor_final = valor - valor_desconto

    # taxa extra
    taxa = taxa_servico(valor_final)
    valor_final = valor_final + taxa

    # evitar negativo
    if valor_final < 0:
        valor_final = 0

    print("Compra realizada com sucesso!")

    mostrar_ticket(nome, plano, valor_final)


# mostrar sócios
def listar_socios():

    print("SÓCIOS CADASTRADOS")

    if len(nomes) == 0:
        print("Nenhum sócio encontrado.")
        return

    for i in range(len(nomes)):

        if mensalidades[i] == True:
            status = "EM DIA"
        else:
            status = "ATRASADO"

        print("----------------------------")
        print("Nome:", nomes[i])
        print("Plano:", planos[i])
        print("Status:", status)


# programa principal
opcao = -1

while opcao != 0:

    menu()

    try:
        opcao = int(input("Escolha uma opção: "))
    except:
        print("Digite apenas números.")
        opcao = -1

    if opcao == 1:
        cadastrar()

    elif opcao == 2:
        vender_ingresso()

    elif opcao == 3:
        listar_socios()

    elif opcao == 0:
        print("Sistema encerrado.")

    else:
        print("Opção inválida.")