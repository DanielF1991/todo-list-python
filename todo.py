# To-Do List em Python (console)
# Desenvolvido com apoio de IA para fins de aprendizado

tarefas = []

def mostrar_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append({"descricao": descricao, "concluida": False})
    print("Tarefa adicionada com sucesso.")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa adicionada.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            status = "✔️" if tarefa["concluida"] else "❌"
            print(f"{i}. [{status}] {tarefa['descricao']}")

def marcar_concluida():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída.")
    except (IndexError, ValueError):
        print("Entrada inválida.")

def remover_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1
        tarefas.pop(indice)
        print("Tarefa removida.")
    except (IndexError, ValueError):
        print("Entrada inválida.")

# Loop principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
Adiciona To-Do List em Python
