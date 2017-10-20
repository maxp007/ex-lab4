# Итератор для удаления дубликатов
class Unique:
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case') and kwargs.get("ignore_case") is not None
        self.items = iter(items)
        self.seen = set()

    def __next__(self):
        while True:
            val = self.items.__next__()
            val_compare = str(val).lower() if self.ignore_case else val

            if val_compare not in self.seen:
                self.seen.add(val_compare)
                return val

    def __iter__(self):
        return self
