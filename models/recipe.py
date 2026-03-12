class Recipe:
    def __init__(self, name, description, ingredients, instructions):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"Recipe: {self.name}\nDescription: {self.description}\nIngredients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}"