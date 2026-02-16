from database import criar_tabela, cadastrar_cliente

criar_tabela()

print("=== SISTEMA CRM ===")

while True:
    print("\n1 - Cadastrar cliente")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        servico = input("Serviço: ")
        origem = input("Origem (instagram/meta/indicacao/whatsapp): ")

        fechou_input = input("Fechou negócio? (s/n): ")
        if fechou_input.lower() == "s":
            fechou = 1
        else:
            fechou = 0

        data_contato = input("Data de contato (AAAA-MM-DD): ")

        valor = 0
        if fechou == 1:
            valor = float(input("Valor do serviço: "))

        cadastrar_cliente(
            nome,
            telefone,
            email,
            servico,
            origem,
            fechou,
            data_contato,
            valor
        )

        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
