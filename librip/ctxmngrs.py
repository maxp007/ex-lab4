# Здесь необходимо реализовать
# контекстный менеджер timer
# Он не принимает аргументов, после выполнения блока он должен вывести время выполнения в секундах
import time


class timer:
    def __enter__(self):
        self.t = time.clock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.clock() - self.t)

class print_one:
    def __init__(self, arg):
        self.arg = arg

    def __enter__(self):
        print(self.arg)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.arg)

# Пример использования
# with timer():
#   sleep(5.5)
#
# После завершения блока должно вывестись в консоль примерно 5.5
