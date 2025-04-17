from pet import Pet

# Create a new pet
my_pet = Pet(input("Enter your pet's name: "))
print(f"Creating pet: {my_pet.name}")

# Interact with the pet
my_pet.eat()
my_pet.play()
my_pet.sleep()

# Teach some tricks
my_pet.train("roll over")
my_pet.train("play dead")

# Show status and tricks
my_pet.get_status()
my_pet.show_tricks()