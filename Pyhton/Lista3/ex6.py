#Simulação de Atendimento Telefônico
print("==ATENDIMENTO TELEFÔNICO==")
print("1 - Suporte Técnico\n2 - Financeiro\n3 - Cancelamento\n4 - Falar com atendente\n5 - Saír")

opcao = input("Digite a opção desejada: ").lower()

match opcao:
    case "suporte" | "suporte técnico" | "1" | "suporte tecnico":
        print("\nEncaminhando ao Suporte Técnico!!!\n")
        input("Digite o que você precisa: ")
        print("Obtendo Resposta, Aguarde!!")

    case "financeiro" | "2":
        print("\nEncaminhando ao Financeiro!!!\n")
        print("1 - Dividas")
        print("2 - Financiamento")
        print("3 - Fatura\n")
        input("O que deseja saber: ")
        print("Aguarde a Respostas, Ja está trabalhando nisso :)")

    case "cancelamento" | "3":
        print("\nEncaminhando ao Cancelamento!!!")
        input("Por que deseja cancelar: ")
        print("Estámos com problemas para realizar o seu cancelamento,\ntente novamente a partir do proximo mês")

    case "falar com atendente" | "atendente" | "4":
        print("\nEncaminhando Ao Atendente!!!")
        input("Bom Dia o Que está ocorrendo: ")
        print("Ah sim!!! Entendi, So que não sou desse setor,\nFique na linha poís vou passar para outro atendente!!!")

    case "sair" | "saír" | "5":
        print("Bom se nao deseja nada, Saindo!!!")

    case _:
        print("Opção errada, Não foi possivel realizar seu atendimento!!!!!")