# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

# Comandos:

# Listar
# Desfazer
# Refazer


while True:
    print("1- Add | 2- Undo | 3- Redo | 4-List | 5- Quit")
    option = int(input("Enter a number from the option above: "))

    if option == 1:
        print("add".upper())

        def add_task(item, list_todo):
            list_todo.append(item)
            return list_todo

        todo = []

        task = input("Typed your task today: ")
        todo_new = add_task(task, todo)
        add_task(task, todo_new)

        continue
    elif option == 2:
        print("undo".upper())
    elif option == 3:
        print("redo".upper())
    elif option == 4:
        print("list".upper())
        print(todo)
    elif option == 5:
        print("quit".upper())
        break


def add_task(item, list_todo):
    list_todo.append(item)
    return list_todo


todo = []

i = 1
while i <= 2:
    task = input("Typed your task today: ")
    todo = add_task(task, todo)  # aqui que ta adicionand o lista
    i += 1

print(todo)
