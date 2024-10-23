class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.tab_cache = {}     # Словарь кэша
        self.queue = []     # Очередь по ключам

    @property
    def cache(self) -> None:
        pass
    def get(self, key: str) -> str:
        self.queue.remove(key)
        self.queue.append(key)
        print()
        return self.tab_cache[key]

    @cache.setter
    def cache(self, key_val: str) -> None:
        if self.capacity == 0:
            self.tab_cache.pop(self.queue[0])
            self.queue.pop(0)
            self.capacity += 1
        self.capacity -= 1
        self.tab_cache[key_val[0]] = key_val[1]
        self.queue.append(key_val[0])

    def print_cache(self) -> None:
        print('\nLRU Cache:')
        for i_key in self.queue:
            print(i_key, ':', self.tab_cache[i_key])


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2


# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")


# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4