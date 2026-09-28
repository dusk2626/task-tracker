"""TaskTracker - aplicação CLI para gerenciamento de tarefas.

Bootcamp II - Engenharia de Software | Fase 2 (Entrega Intermediária)
"""

tarefas = []

PRIORIDADES_VALIDAS = ("Alta", "Média", "Media", "Baixa")


def ler_titulo_valido():
    """Solicita o título até que um valor não vazio (após strip) seja informado."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título não pode ser vazio. Digite um título válido.")


def ler_prioridade_valida():
    """Solicita a prioridade até que uma das opções válidas seja informada."""
    while True:
        prioridade = input("Prioridade (Alta/Média/Baixa): ").strip()
        if prioridade in PRIORIDADES_VALIDAS:
            return prioridade
        print("Erro: prioridade inválida! Use apenas: Alta, Média (ou Media) ou Baixa.")


def exibir_menu():
    print("\n===== TASKTRACKER =====")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("=======================")


def cadastrar_tarefa():
    print("\n--- Nova tarefa ---")
    titulo = ler_titulo_valido()
    descricao = input("Descrição: ").strip()
    prioridade = ler_prioridade_valida()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas():
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"[{indice}] Título: {tarefa['titulo']}")
        print(f"    Descrição: {tarefa['descricao']}")
        print(f"    Prioridade: {tarefa['prioridade']}")
        print(f"    Data limite: {tarefa['data_limite']}")
        print(f"    Status: {tarefa['status']}")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            print("Encerrando a aplicação. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
