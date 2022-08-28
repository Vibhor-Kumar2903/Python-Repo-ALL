import random

class Person:
    def __init__(self, firstName, lastName, health, status):
        self.firstName = firstName
        self.lastName = lastName
        self.health = health
        self.status = status

    def introduce(self):
        print("My name is {} {}".format(self.firstName, self.lastName))

    def emtn(self):
        emtn = random.randrange(1,3)
        if emtn == 1:
            print("{} is happy today.".format(self.firstName))

        elif emtn == 2:
            print("{} is sad today.".format(self.firstName))

    def health_status(self):
        if self.health <= 100 and self.health >75:
            print("{} is quiet healthy".format(self.firstName))

        elif self.health <= 75 and self.health >50:
            print("{} is fine".format(self.firstName))

        elif self.health <= 50 :
            print("{} is unhealthy".format(self.firstName))

Vibhor = Person("Vibhor", "Kumar", 97, status=True)
Vishal = Person("Vishal", "Singh", 74, status=True)
Navin = Person("Navin", "Tiwari", 49, status=False)

print("{} is my friend ? {}".format(Vibhor.firstName, Vibhor.status))
print("{} is my friend ? {}".format(Vishal.firstName, Vishal.status))
print("{} is my friend ? {}".format(Navin.firstName, Navin.status))

Vibhor.introduce()
Vishal.introduce()
Navin.introduce()

Vibhor.health_status()
Vishal.health_status()
Navin.health_status()

class Enemy(Person):
    def __init__(self, weapon, firstName, lastName, health, status):
        super().__init__(firstName, lastName, health, status)
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == "rock":
            other.health -= 10
        elif self.weapon == "stick":
            other.health -=5
        print(other.health)

    def insult(self, other):
        if other.health <=60:
            print("{} you are tiered and weak".format(other.firstName))

    def steal(self, other):
        print("{} your stuff is hear".format(other.firstName))
        if other.status == True:
            other.status = False

Alex = Enemy("rock","Alex", "Wayne", 75, status=False)

Alex.insult(Vibhor)
Alex.insult(Vishal)
Alex.insult(Navin)

Alex.steal(Navin)

