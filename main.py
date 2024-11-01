#Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.
#Исходные данные:
#Есть класс Fighter, представляющий бойца.
#Есть класс Monster, представляющий монстра.
#Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.

from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abstractmethod
    def attack(self, fighter_name):
        pass

class Sword(Weapon):
    def attack(self, fighter_name):
        print(f"{fighter_name}, The Fighter attacks with a Sword!")


class Bow(Weapon):
    def attack(self, fighter_name):
        print(f"{fighter_name}, The Fighter attacks with a Bow!")


class Fighter():
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name}, The Fighter has switched to {self.weapon}")

    def __str__(self):
            return self.name

    def fight(self):
        self.weapon.attack(self.name)
        print("The Monster is defeated!")


class Monster():
    def __init__(self):
        pass


sword = Sword("The Great Sword")
bow = Bow("The Bow of the Wild")

fighter = Fighter("Arthur", sword)
fighter.fight()
fighter.change_weapon(bow)
fighter.fight()


