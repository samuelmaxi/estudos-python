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

todo = []
last_task = []
while True:
    print("1- Add | 2- Undo | 3- Redo | 4-List | 5- Quit")
    option = int(input("Enter a number from the option above: "))

    if option == 1:
        print("add".upper())

        def add_task(item, list_todo):
            list_todo.append(item)
            return list_todo

        task = input("Typed your task today: ")
        todo_new = add_task(task, todo)

        continue
    elif option == 2:
        print("undo".upper())
        last_task = todo
        last_task.pop()
    elif option == 3:
        print("redo".upper())
        todo.append(task)
    elif option == 4:
        print("list".upper())
        print(todo)
    elif option == 5:
        print("quit".upper())
        break
