#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = None
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = input("введите путь к файлу \n")
# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path, encoding='utf-8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return list(sorted(unique(field(arg, "job-name"), ignore_case=True)))

@print_result
def f2(arg):
    return list(filter(lambda x: "программист" in x, arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))

@print_result
def f4(arg):
    sal_list = list(gen_random(100000, 200000, len(arg)))
    worklist = iter(map(lambda x: x + " зарплата", arg))
    return ["{} {}".format(work, sal) for (work, sal) in zip(worklist, sal_list)]

with timer():
    f4(f3(f2(f1(data))))
