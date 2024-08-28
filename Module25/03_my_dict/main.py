class MyDict(dict):
    def get(self, __key):
        if __key in self:
            return self[__key]
        else:
            return 0


my_dict = MyDict({1: 11, 2: 22, 3: 33, 'abc': 'ldsakfg', 'qwerty': [1, 2, 3]})

print(my_dict.get(1))
print(my_dict.get(22))
print(my_dict.get(3))
print(my_dict.get('ldsakfg'))
print(my_dict.get('qwerty'))
