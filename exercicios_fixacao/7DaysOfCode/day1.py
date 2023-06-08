# implementar uma versão simplificada de uma lista de compras usando arrays.
#   A lista deve permitir adicionar novos itens,
#   remover itens e
#   listar todos os itens.

# Ao adicionar um novo item, o usuário deve inserir o nome do produto e a quantidade desejada. Ao remover um item, o usuário deve especificar o nome do produto. Por fim, ao listar todos os itens, a lista deve exibir o nome do produto e a quantidade em um formato legível.

def add_itens(item, amout, new_list, new_amount_list):
    new_list.append(item)
    new_amount_list.append(amout)
    return new_list, new_amount_list


def del_itens(del_item, new_list, new_amount_list):
    for i, item in enumerate(new_list):
        if item == del_item:
            new_list.remove(item)
            del new_amount_list[i]
            break

    return new_list, new_amount_list


def show_list(new_list, new_amount_list):
    print('LISTA DE COMPRAS')
    for i, (item, amout) in enumerate(zip(new_list, new_amount_list), start=1):
        print(f'{i}-{item} x{amout}')


my_list = []
my_amount_list = []

# print(show_list(my_list))
add_itens('limão', 3, my_list, my_amount_list)
add_itens('limão', 5, my_list, my_amount_list)
add_itens('tangerina', 2, my_list, my_amount_list)
add_itens('maçã', 1, my_list, my_amount_list)
add_itens('melancia', 7, my_list, my_amount_list)
add_itens('banana', 9, my_list, my_amount_list)
add_itens('coco', 10, my_list, my_amount_list)
show_list(my_list, my_amount_list)
