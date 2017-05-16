class LivingThing:
    pass

class Plant(LivingThing):
    can_walk = "No"

class Animal(LivingThing):

    can_fly = "No"
    can_walk = "Yes"

    def __str__(self):
        return (self.name)

class Dog(Animal):

    def __init__(self):
        self.name = "Fido"

    def __str__(self):
        return ("My name is "+self.name+" and I am a dog")

class Cat(Animal):

    name = "Meredith"

    def __init__(self):
        pass

    def changeAllNames(self,newname):
        Cat.name = newname

class Bird(Animal):

    can_fly = "Yes"
    name = "Bob"

    def __init__(self):
        self.name = ""
        self.legs = 2
        self.wings = 2
        can_fly = "Yes"

class Penguin(Bird):

    can_fly = "No"

class Fish(Animal):

    can_walk = "No"

    def __init__(self,name):
        self.name = name

def main():

    dog1 = Dog()
    dog2 = Dog()
    print(dog1.name)
    print(dog2.name)

    cat1 = Cat()
    cat2 = Cat()
    print(cat1.name)
    print(cat2.name)

    cat2.name = "Sylvester"
    print(cat1.name)
    print(cat2.name)

    cat3 = Cat()
    print(cat1.name)
    print(cat2.name)
    print(cat3.name)
    
    cat1.changeAllNames("Puddy Tat")
    print(cat1.name)
    print(cat2.name)
    print(cat3.name)

    bird1 = Bird()
    bird1.name = "Tweety"
    bird2 = Bird()
    bird2.name = "Big Bird"
    print(bird1.name)
    print(bird1.legs)
    print(bird1.wings)

    print(cat3.can_fly)
    print(dog1.can_fly)
    print(bird1.can_fly)
    print(bird2.can_fly)

    print(bird1.name)
    print(bird2.name)
    bird3 = Bird()
    print(bird3.name)

    penguin1 = Penguin()
    penguin1.name = "Opus"
    print(penguin1.name)
    print(penguin1.can_fly)

    fish1 = Fish("Nemo")
    print(fish1.can_fly)
    print(fish1.can_walk)
    
    print("\n\n")

    print(dog1)
    print(cat2)
    print(bird1)
    print(fish1)




main()
