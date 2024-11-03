# TODO Напишите функцию для поиска индекса товара

def product_index_search(list, item):
    index=0
    for ind, it in enumerate(list):
        if it==item:
            return ind
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:

    index_item = product_index_search(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
