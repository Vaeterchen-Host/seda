"""This file defines classes"""

# All classes about food.

from typing import Self


class NutrientSummary:
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
    def __init__(self, id, name, type, nutrients_per_100g: NutrientSummary):
        self._id = id
        self._name = name
        self._type = type
        self._nutrients_per_100g = nutrients_per_100g


class MealItem:
    def __init__(self, food: Food, amount_in_gramm):
        self._food = food
        self._amount_in_gramm = amount_in_gramm


class Meal:
    def __init__(self, id, name, items: list[MealItem]):
        self._id = id
        self._name = name
        self._items = items


# All classes for logging


class FoodLog:
    def __init__(self, id, food, amount_in_gramm, timestamp):
        self._id = id
        self._food = food
        self._amount_in_gramm = amount_in_gramm
        self._timestamp = timestamp


class MealLog:
    def __init__(self, id, meal, amount_in_gramm, timestamp):
        self._id = id
        self._meal = meal
        self._amount_in_gramm = amount_in_gramm
        self._timestamp = timestamp


class WaterLog:
    def __init__(self, id, amount_in_ml, timestamp):
        self._id = id
        self._amount_in_ml = amount_in_ml
        self._timestamp = timestamp


class WeightLog:
    def __init__(self, id, weight_in_kg, timestamp):
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
