# Design a class hierarchy for different types of food items. Include a base class Food and subclasses such as Fruit, Vegetable, and Meat. Each subclass should have methods to describe its taste and nutritional value.

class Food:
    def taste(self):
        pass

    def nutritional_value(self):
        pass

class Fruit(Food):
    def taste(self):
        return "Sweet"

    def nutritional_value(self):
        return "High in vitamins and fiber"

class Vegetable(Food):
    def taste(self):
        return "Varies (can be sweet or bitter)"

    def nutritional_value(self):
        return "High in vitamins and minerals"

class Meat(Food):
    def taste(self):
        return "Savory"

    def nutritional_value(self):
        return "High in protein and fats"
