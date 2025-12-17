#Zoo
class Food:
    def __init__(self, name):
        self.name=name 
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_hungry = True

    def eat(self, food):
        raise NotImplementedError

class Carnivore(Animal):
    def eat(self, food):
        if not self.is_hungry:
            print(f"{self.name} is not hungry")
            return

        if food.name == "Meat":
            print(f"{self.name} ({self.species}) ate {food.name} ")
            self.is_hungry = False
        else:
            print(f"{self.name} does not eat {food.name} ")

class Herbivore(Animal):
    def eat(self, food):
        if not self.is_hungry:
            print(f"{self.name} is not hungry")
            return

        if food.name in ["Grass", "Fruits"]:
            print(f"{self.name} ({self.species}) ate {food.name} ")
            self.is_hungry = False
        else:
            print(f"{self.name} does not eat {food.name} ")

class Cage:
    def __init__(self, number):
        self.number = number
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} is in  {self.number} cage")
class Worker:
    def __init__(self, name):
        self.name = name

    def feed_animals(self, animals, food):
        print(f"{self.name} feeds with {food.name}")
        for animal in animals:
            animal.eat(food)

meat = Food("Meat")
grass = Food("Grass")
fruit = Food("Fruits")

lion = Carnivore("Simba", "Lion")
tiger = Carnivore("Sherxan", "Tiger")
elephant = Herbivore("Dambo", "Elephant")
monkey = Herbivore("Chiko", "Monkey")

cage1 = Cage(1)
cage1.add_animal(lion)
cage1.add_animal(elephant)

cage2 = Cage(2)
cage2.add_animal(tiger)
cage2.add_animal(monkey)

worker1 = Worker("Aram")
worker2 = Worker("Vahe")

worker1.feed_animals(cage1.animals, grass)
worker1.feed_animals(cage1.animals, meat)
worker2.feed_animals(cage2.animals, fruit)
worker2.feed_animals(cage2.animals, meat)
