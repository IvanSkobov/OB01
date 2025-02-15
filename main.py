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
