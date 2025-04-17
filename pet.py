class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        print(f"{self.name} is eating... ")
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)

    def sleep(self):
        print(f"{self.name} is sleeping... ")
        self.energy = min(self.energy + 5, 10)

    def play(self):
        if self.energy <= 0:
            print(f"{self.name} is too tired to play!")
        else:
            print(f"{self.name} is playing... ")
            self.energy = max(self.energy - 2, 0)
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)

    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks if self.tricks else 'None yet!'}\n")

    def train(self, trick):
        print(f"{self.name} is learning a new trick: {trick}! ")
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 1, 10)

    def show_tricks(self):
        print(f"{self.name} knows the following tricks: {', '.join(self.tricks) if self.tricks else 'No tricks yet!'}")