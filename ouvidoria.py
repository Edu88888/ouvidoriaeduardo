from ouvidoria_db import (
    listar_manifestacoes,
    listar_por_tipo,
    criar_manifestacao,
    contar_manifestacoes,
    buscar_por_id,
    remover_manifestacao
)

while True:
    print("\nOuvidoria Eduardo ")
    print("1 - Listar Todas as Manifestações")
    print("2 - Listar Manifestações por Tipo")
    print("3 - Criar Nova Manifestação")
    print("4 - Exibir Quantidade de Manifestações")
    print("5 - Pesquisar Manifestação por Código")
    print("6 - Excluir Manifestação pelo Código")
    print("7 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        manifestacoes = listar_manifestacoes()
        if len(manifestacoes) == 0:
            print("Nenhuma manifestação encontrada.")
        else:
            for m in manifestacoes:
                print(f"{m[0]} - [{m[1]}] {m[2]}")

    elif escolha == "2":
        tipo = input("Digite o tipo (reclamacao, elogio, sugestao): ")
        manifestacoes = listar_por_tipo(tipo)
        if len(manifestacoes) == 0:
            print(f"Nenhuma manifestação do tipo '{tipo}' encontrada.")
        else:
            for m in manifestacoes:
                print(f"{m[0]} - [{m[1]}] {m[2]}")

    elif escolha == "3":
        tipo = input("Tipo (reclamacao, elogio, sugestao): ")
        descricao = input("Descrição da manifestação: ")
        criar_manifestacao(tipo, descricao)
        print("Manifestação criada com sucesso!")

    elif escolha == "4":
        total = contar_manifestacoes()
        print(f"Existem {total} manifestações cadastradas.")

    elif escolha == "5":
        id_busca = input("Digite o código da manifestação: ")
        resultado = buscar_por_id(int(id_busca))
        if resultado:
            print(f"{resultado[0]} - [{resultado[1]}] {resultado[2]}")
        else:
            print("Manifestação não encontrada.")

    elif escolha == "6":
        id_remover = input("Digite o código da manifestação para excluir: ")
        confirmar = input("Tem certeza que deseja remover? (s): ")
        if confirmar == "s":
            sucesso = remover_manifestacao(int(id_remover))
            if sucesso:
                print("Manifestação removida com sucesso.")
            else:
                print("Manifestação não encontrada.")
        else:
            print("Remoção cancelada.")

    elif escolha == "7":
        print("Obrigado por usar a Ouvidoria Eduardo.")
        break

    else:
        print("Escolha uma opção entre 1 e 7.")