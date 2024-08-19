from basic_element import Water, Air, Fire, Earth, Lightning

water = Water()
air = Air()
fire = Fire()
earth = Earth()
lightning = Lightning()

ice = water + air
steam = water + fire
dirt = water + earth
heat = air + fire
dust = air + earth
lava = fire + earth
storm = lightning + water
magnet = lightning + air
blast = lightning + fire
crystal = lightning + earth

print(crystal.name)
print(magnet.name)
print(ice.name)