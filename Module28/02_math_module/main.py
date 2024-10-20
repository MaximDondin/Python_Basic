import math
class MyMath:
    @classmethod
    def circle_len(cls, radius: float) -> float:
        return 2 * math.pi * radius
    @classmethod
    def circle_sq(cls, radius: float) -> float:
        return math.pi * radius ** 2
    @classmethod
    def volume_cube(cls, lenght: float) -> float:
        return lenght ** 3
    @classmethod
    def area_sphere(cls, radius: float) -> float:
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.volume_cube(lenght=6)
res_4 = MyMath.area_sphere(radius=8)
print('вычисление длины окружности:', res_1)
print('вычисление площади окружности:', res_2)
print('вычисление объёма куба:', res_3)
print('вычисление площади поверхности сферы:', res_4)