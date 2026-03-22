"""This file defines classes"""

# All classes about food.


class NutrientSummary:
    """This class defines the nutrient summary of a food."""

    def __init__(
        self,
        calorie,
        fat,
        saturated_fat,
        carbohydrate,
        fibre,
        sugar,
        protein,
        salt,
        sodium,
    ):
        """This is the constructor of NutrientSummary."""
        self._calorie = calorie
        self._fat = fat
        self._saturated_fat = saturated_fat
        self._carbohydrate = carbohydrate
        self._fibre = fibre
        self._sugar = sugar
        self._protein = protein
        self._salt = salt
        self._sodium = sodium


class Food:
    """This class defines the food."""

    def __init__(self, food_id, name, food_type, nutrients_per_100g: NutrientSummary):
        """This is the constructor of Food."""
        self._id = food_id
        self._name = name
        self._type = food_type
        self._nutrients_per_100g = nutrients_per_100g


class MealItem:
    """This class defines the meal item."""

    def __init__(self, food: Food, amount_in_gramm):
        """This is the constructor of MealItem."""
        self._food = food
        self._amount_in_gramm = amount_in_gramm


class Meal:
    """This class defines the meal."""

    def __init__(self, meal_id, name, items: list[MealItem]):
        """This is the constructor of Meal."""
        self._id = meal_id
        self._name = name
        self._items = items


# All classes for logging


class FoodLog:
    """This class defines the food log."""

    def __init__(self, food_log_id, food, amount_in_gramm, timestamp):
        """This is the constructor of FoodLog."""
        self._id = food_log_id
        self._food = food
        self._amount_in_gramm = amount_in_gramm
        self._timestamp = timestamp


class MealLog:
    """This class defines the meal log."""

    def __init__(self, meal_log_id, meal, amount_in_gramm, timestamp):
        """This is the constructor of MealLog."""
        self._id = meal_log_id
        self._meal = meal
        self._amount_in_gramm = amount_in_gramm
        self._timestamp = timestamp


class WaterLog:
    """This class defines the water log."""

    def __init__(self, water_log_id, amount_in_ml, timestamp):
        """This is the constructor of WaterLog."""
        self._id = water_log_id
        self._amount_in_ml = amount_in_ml
        self._timestamp = timestamp


class WeightLog:
    """This class defines weightlog."""

    def __init__(self, weight_log_id, weight_in_kg, timestamp):
        """This is the constructor of weightlog."""
        self._id = weight_log_id
        self._weight_in_kg = weight_in_kg
        self._timestamp = timestamp


# User class. Somehow the main node of all classes.


class User:
    """This is the class User."""

    def __init__(
        self,
        user_id,
        name,
        birthdate,
        height_in_cm,
        gender,
        fitness_lvl,
        water: list[WaterLog],
        weight: list[WeightLog],
        food: list[FoodLog],
        meal: list[MealLog],
    ):
        """This is the constructor of User."""
        self._id = user_id
        self._name = name
        self._birthdate = birthdate
        self._height_in_cm = height_in_cm
        self._gender = gender
        self._fitness_lvl = fitness_lvl
        self._water = water
        self._weight = weight
        self._food = food
        self._meal = meal
