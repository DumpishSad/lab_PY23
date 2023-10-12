# TODO Напишите функцию для поиска индекса товара
def find_ind(items, string_):
    for i in range(0, len(items)):
        if items[i] == string_:
            return i


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
find_ind(items_list, 'банан')
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_ind(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
