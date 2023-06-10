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


def add_task(task, list_todo=None):
    if list_todo is None:
        list_todo = []
    list_todo.append(task)
    return list_todo


todo = []

task = input("Trype your taks: ")
todo_list = add_task(task, todo)
add_task("JANTAR", todo_list)
add_task("comer", todo_list)
add_task("dormir", todo_list)

print(todo_list)
