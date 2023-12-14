from pet import Pet

class Dog(Pet):
    def __init__(self, name, age, breed, dog_breed):
        super().__init__(name, age, breed)
        self.dog_breed = dog_breed

    def __str__(self):
        return f"Dog(dog_breed={self.dog_breed}) {super().__str__()}"
