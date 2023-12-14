class Pet:
    def __init__(self, name, age, breed):
        self.Name = name
        self.Age = age
        self.Breed = breed

    def __str__(self):
        return f"{self.Name}, {self.Age} years old, {self.Breed}"