class Warior(object):
    def __init__(self, name, health, attack_power, defense, speed):
        self.health = health
        self.name = name
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed

    def sleep(self):
        print(f"{self.name} Лег спать")
        self.health += 10

    def eat(self):
        print(f"{self.name} Поел")
        self.attack_power += 5

    def hit(self, enemy):
        print(f"{self.name} Нанес {enemy.attack_power} урона")
        enemy.health -= enemy.attack_power
        self.attack_power -= 1

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Здоровье: {self.health}")
        print(f"Сила атаки: {self.attack_power}")
        print(f"Защита: {self.defense}")
        print(f"Скорость: {self.speed}")
        print("\n")


war1 = Warior("Ivan", 100, 10, 10, 10)
war2 = Warior("Vasya", 100, 5, 15, 10)

print(war1.info())
print(war2.info())
war1.sleep()
war1.eat()
war1.hit(war2)

war2.sleep()
war2.eat()
war2.hit(war1)

print(war1.info())
print(war2.info())

