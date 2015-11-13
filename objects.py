import random
import sys
import os


class Creature:
    name = ""
    height = 0
    weight = 0
    sound = 0

    # double underscore means its private

    def __init__(self, name, height, weight, sound):
        self.name = name
        self.height = height
        self.weight = weight
        self.sound = sound

    def set_name(self, name):
        self.name = name  # sets the __name value to ""

    def get_name(self):
        return self.name  # gets the value from __name since it is private

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def set_sound(self, sound):
        self.sound = sound

    def get_sound(self):
        return self.sound

    def get_type(self):
        print("Creature")

    def toString(self):
        return "{} is {} inches tall, weighs {} lbs, and says {}".format(self.name,
                                                                         self.height,
                                                                         self.weight,
                                                                         self.sound)


human = Creature("Milo", 58, 140, "hello")
print(human.toString())


class Creature2(Creature):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Creature2, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Lesser Creature")

    def toString(self):
        return "{} is {} inches tall, weighs {} lbs, says {}, and is owned by {}".format(self.name,
                                                                                         self.height,
                                                                                         self.weight,
                                                                                         self.sound,
                                                                                         self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


spot = Creature2("Spot", 24, 75, "bark", 'Milo')
print(spot.toString())


class CreatureTesting:
    def get_type(self, creature):
        creature.get_type()


test_creatures = CreatureTesting()
test_creatures.get_type(human)
test_creatures.get_type(spot)

spot.multiple_sounds(4)
