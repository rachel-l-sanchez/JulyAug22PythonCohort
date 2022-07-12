class Pet:
    def __init__(self,name, type, tricks, health, energy):
        self.health = health
        self.type = "dog"
        self.tricks = "shake"
        self.name = "Enzo"
        self.health = health
        self.energy = energy
    
    # method to print the object clearly
    def __repr__(self) -> str:
        return f"Bellatrix: {self.name}, {self.health}, {self.type}, {self.tricks}, {self.energy}"
    
    # sleep() - increases the pets energy by 25
    def sleep(self, energy):
        self.energy = energy
        energy *= 1.25
        
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self, energy, health):
        self.energy += 5
        health += 10
        
    # play() - increases the pet's health by 5
    def play(self, health):
        self.health += 5
    # noise() - prints out the pet's sound
    def noise(self, sound):
        self.sound = 'Woooof Wooof'

class Ninja(Pet):
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food,pet, name, type, tricks, health, energy):
        super().__init__(name,type,tricks, health, energy)
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = "Kibble"
        self.pet = Pet(name="Enzo",type="dog",tricks="shake", health="100",energy= "75")
    
    def __repr__(self) -> str:
        return f"Monty: {self.first_name}, {self.last_name}, {self.treats}, {self.pet_food}"
    
    # walk() - walks the ninja's pet invoking the pet
    def walk(self):
        walk = self.pet.play(self.health)
        return self
        
    # feed() - feeds the ninja's pet invoking the eat method
    def feed(self):
        self.feed = self.pet.eat
        return self
        
    # bathe() - cleans the ninja's pet invoking
    # the pet noise() method
    def bathe(self):
        self.bathe = self.pet.noise
        return self

bellatrix = Pet('Bellatrix', 'dog', 'shake', 100, 75)
monty = Ninja('monty','Python', 'Peanut butter dog treat', 'Kibble', 'Enzo', "Enzo", "dog", "shake", "100", "75")
monty.pet = bellatrix
monty.walk().feed().bathe()