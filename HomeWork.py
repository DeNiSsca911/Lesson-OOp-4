from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {type(weapon).__name__.lower()}.")

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "У бойца нет оружия!"

# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name

    def defeated(self):
        print(f"{self.name} побежден!")

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    print(fighter.attack())
    monster.defeated()

# Пример использования
if __name__ == "__main__":
    fighter = Fighter("Валера")
    monster = Monster("Гоблин")

    # Боец с мечом
    sword = Sword()
    fighter.changeWeapon(sword)
    battle(fighter, monster)

    # Боец с луком
    bow = Bow()
    fighter.changeWeapon(bow)
    battle(fighter, monster)
