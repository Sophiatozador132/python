from lib import funcoes
import database

def menu():
    print("\n=== MENU ===")
    print("1. Cadastrar jogador")
    print("2. Consultar jogador")
    print("3. Atualizar jogador")
    print("4. Apagar jogador")
    print("5. Listar todos os jogadores")
    print("6. Cadastrar time")
    print("7. Atualizar time")
    print("8. Listar todos os times")
    print("9. Relatórios")
    print("0. Sair")

def main():
    conn = database.conectar_banco()
    database.criar_tabelas(conn)
    opcao = None

    while opcao != '0':
        menu()
        opcao = input("\nDigite a opção desejada: ")

        if opcao == '1':
            nome = input("Digite o nome do jogador: ")
            time_id = input("Digite o ID do time do jogador: ")
            funcoes.adicionar_jogador(conn, nome, time_id)

        elif opcao == '2':
            jogador_id = input("Digite o ID do jogador que deseja consultar: ")
            jogador = funcoes.consultar_jogador(conn, jogador_id)
            if jogador:
                print("ID:", jogador[0])
                print("Nome:", jogador[1])
                print("ID do Time:", jogador[2])
            else:
                print("Jogador não encontrado.")

        elif opcao == '3':
            jogador_id = input("Digite o ID do jogador que deseja atualizar: ")
            nome = input("Digite o novo nome do jogador: ")
            time_id = input("Digite o novo ID do time do jogador: ")
            funcoes.atualizar_jogador(conn, jogador_id, nome, time_id)

        elif opcao == '4':
            jogador_id = input("Digite o ID do jogador que deseja apagar: ")
            funcoes.apagar_jogador(conn, jogador_id)

        elif opcao == '5':
            jogadores = funcoes.listar_jogadores(conn)
            for jogador in jogadores:
                print("ID:", jogador[0])
                print("Nome:", jogador[1])
                print("ID do Time:", jogador[2])

        elif opcao == '6':
            nome_time = input("Digite o nome do time: ")
            funcoes.adicionar_time(conn, nome_time)

        elif opcao == '7':
            time_id = input("Digite o ID do time que deseja atualizar: ")
            novo_nome_time = input("Digite o novo nome do time: ")
            funcoes.atualizar_time(conn, time_id, novo_nome_time)

        elif opcao == '8':
            times = funcoes.listar_times(conn)
            for time in times:
                print("ID:", time[0])
                print("Nome:", time[1])

        elif opcao == '9':
            print("\nRelatórios:")
            # Implement
def salvar_nomes_jogadores(nomes):
    try:
        with open("nomes_jogadores.txt", "w") as arquivo:
            for nome in nomes:
                arquivo.write(nome + "\n")
        print("Nomes dos jogadores salvos com sucesso!")
    except Exception as e:
        print("Ocorreu um erro ao salvar os nomes dos jogadores:", str(e))

# Exemplo de uso:
nomes_jogadores = ["Neymar", "Messi", "Cristiano Ronaldo", "Mbappé"]
salvar_nomes_jogadores(nomes_jogadores)

if __name__ == "__main__":
    main()