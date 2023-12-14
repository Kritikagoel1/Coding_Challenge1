class InvalidPetAgeError(Exception):
    def __init__(self, message="Invalid pet age. Age should be a positive integer."):
        self.message = message
        super().__init__(self.message)

class Pet:
    def __init__(self, name, age, breed):
        self.Name = name
        self.set_age(age)  # Use the setter to validate age
        self.Breed = breed

    def set_age(self, age):
        try:
            age = int(age)
            if age <= 0:
                raise InvalidPetAgeError()
            self.Age = age
        except ValueError:
            raise InvalidPetAgeError()

# Example usage:
try:
    pet_name = input("Enter pet name: ")
    pet_age = input("Enter pet age: ")

    new_pet = Pet(pet_name, pet_age, "Mixed Breed")
    print(f"Pet {new_pet.Name} added to the shelter. Age: {new_pet.Age}")
except InvalidPetAgeError as e:
    print(f"Error: {e}")



