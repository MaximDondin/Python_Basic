import random
class Warrior:
  name = 'Воин'
  hp = 100
  def damage(self):
    self.hp -= 20

warrior1 = Warrior()
warrior2 = Warrior()

while warrior1.hp > 0 and warrior2.hp > 0:
  move = random.randint(1,2)
  print(f"Удар нанёс: Воин {move}")
  if move == 1:
    #warrior2.damage -= 20
    warrior2.damage()
    print(f"Воин 2: осталось здоровья - {warrior2.hp} hp\n")
  else:
    #warrior1.damage -= 20
    warrior1.damage()
    print(f"Воин 1: осталось здоровья - {warrior1.hp} hp\n")
if warrior1.hp == 0:
  print("Победил Воин 2")
else:
  print("Победил Воин 1")