"""This file defines classes"""

# All classes about food.

# Self is used for type hinting when a class references itself.
from typing import Self  # do i need t


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

    def __init__(self, id, name, type, nutrients_per_100g: NutrientSummary):
        """This is the constructor of Food."""
        self._id = id
        self._name = name
        self._type = type
        self._nutrients_per_100g = nutrients_per_100g


class MealItem:
    """This class defines the meal item."""

    def __init__(self, food: Food, amount_in_gramm):
        """This is the constructor of MealItem."""
        self._food = food
        self._amount_in_gramm = amount_in_gramm


class Meal:
    """This class defines the meal."""

    def __init__(self, id, name, items: list[MealItem]):
        """This is the constructor of Meal."""
        self._id = id
        self._name = name
        self._items = items


# All classes for logging


class FoodLog:
    """This class defines the food log."""

    def __init__(self, id, food, amount_in_gramm, timestamp):
        """This is the constructor of FoodLog."""
        self._id = id
        self._food = food
        self._amount_in_gramm = amount_in_gramm
        self._timestamp = timestamp


class MealLog:
    """This class defines the meal log."""

    def __init__(self, id, meal, amount_in_gramm, timestamp):
        """This is the constructor of MealLog."""
        self._id = id
        self._meal = meal
        self._amount_in_gramm = amount_in_gramm
        self._timestamp = timestamp


class WaterLog:
    """This class defines the water log."""

    def __init__(self, id, amount_in_ml, timestamp):
        """This is the constructor of WaterLog."""
        self._id = id
        self._amount_in_ml = amount_in_ml
        self._timestamp = timestamp


class WeightLog:
    """This class defines weightlog."""

    def __init__(self, id, weight_in_kg, timestamp):
        """This is the constructor of weightlog."""
        self._id = id
        self._weight_in_kg = weight_in_kg
        self._timestamp = timestamp


# User class. Somehow the main node of all classes.


class User:
    """This is the class User."""

    def __init__(
        self,
        id,
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
        self._id = id
        self._name = name
        self._birthdate = birthdate
        self._height_in_cm = height_in_cm
        self._gender = gender
        self._fitness_lvl = fitness_lvl
        self._water = water
        self._weight = weight
        self._food = food
        self._meal = meal
