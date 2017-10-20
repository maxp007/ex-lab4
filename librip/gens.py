from random import randint


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for el in items:
            if el.get(args[0]) is not None:
                yield el.get(args[0])
    else:
        for el in items:
            if len(set(args) & set(el.keys())) != 0:
                yield {key: el.get(key) for key in args if el.get(key) is not None}


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки

def gen_random(begin, end, num_count):
    for x in range(num_count):
        yield randint(begin, end)

    # Необходимо реализовать генератор