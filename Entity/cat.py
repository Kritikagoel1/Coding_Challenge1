from pet import Pet

class Cat(Pet):
    def __init__(self, name, age, breed, cat_color):
        super().__init__(name, age, breed)
        self.cat_color = cat_color

    def __str__(self):
        return f"Cat(cat_color={self.cat_color}) {super().__str__()}"
