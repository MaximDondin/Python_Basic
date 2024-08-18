from new_element import Ice, Storm, Steam, Dirt, Dust, Heat, Lava, Crystal, Magnet, Blast
class Water:
    name = 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Ice()        # Поменял Storm на холод т.к. шторм = вода + молния
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Lightning):
            return Storm()
        else:
            return None
class Air:
    name = 'Воздух'
    def __add__(self, other):
        if isinstance(other, Water):
            return Ice()      # Поменял Storm на холод т.к. шторм = вода + молния
        elif isinstance(other, Fire):
            return Heat()       # Поменял Lightning на жару т.к. молнию взял в базовый элемент
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Lightning):
            return Magnet()
        else:
            return None
class Fire:
    name = 'Огонь'
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Heat()       # Поменял Lightning на жару т.к. молнию взял в базовый элемент
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Lightning):
            return Blast()
        else:
            return None
class Earth:
    name = 'Земля'
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Lightning):
            return Crystal()
        else:
            return None
class Lightning:
    name = 'Молния'
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Air):
            return Magnet()
        elif isinstance(other, Fire):
            return Blast()
        elif isinstance(other, Earth):
            return Crystal()
        else:
            return None