# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Tobias Mignat & Sabine Steverding
# See LICENSE.md for the full license text.

"""This module contains the food and meal classes for the application."""

from datetime import datetime
from dataclasses import dataclass, fields
from typing import Optional


# Helper functions for dataclass initialization and log validation. ai-generated.
def _zero_dataclass(cls):
    """Create a zero-valued dataclass instance for nutrient objects."""
    return cls(**{field.name: 0 for field in fields(cls)})


# ai-generated content start: helper function for validating log lists. ai-generated.
def _validate_log_list(logs, log_type, label):
    """Validate that logs is a list containing only the expected log type."""
    if not isinstance(logs, list) or not all(isinstance(log, log_type) for log in logs):
        raise ValueError(f"{label} must be a list of {log_type.__name__} objects.")
    return logs


def _validate_non_negative(values):
    """Validate that nutrient values are non-negative."""
    for name, value in values.items():
        if value is not None and value < 0:
            raise ValueError(f"{name} must be non-negative. Got {value}.")


# All classes about food.


@dataclass
class BigSeven:
    """This class defines the nutrient summary of a food."""

    fat: Optional[float]
    saturated_fat: Optional[float]
    carbohydrate: Optional[float]
    fibre: Optional[float]
    sugar: Optional[float]
    protein: Optional[float]
    salt: Optional[float]

    def __post_init__(self):
        """Validate that the nutrient values are non-negative."""
        _validate_non_negative(
            {
                "fat": self.fat,
                "saturated_fat": self.saturated_fat,
                "carbohydrate": self.carbohydrate,
                "fibre": self.fibre,
                "sugar": self.sugar,
                "protein": self.protein,
                "salt": self.salt,
            }
        )


@dataclass
class NutrientSummary:
    """This class defines the nutrient summary outside of the big seven."""

    water: Optional[float]  # in g per 100g
    monounsaturated_fat: Optional[float]  # in g per 100g
    polyunsaturated_fat: Optional[float]  # in g per 100g
    omega_3: Optional[float]  # in g per 100g
    omega_6: Optional[float]  # in g per 100g
    starch: Optional[float]  # in g per 100g
    alcohol: Optional[float]  # in g per 100g
    sodium: Optional[float]  # in mg per 100g
    cholesterol: Optional[float]  # in mg per 100g
    potassium: Optional[float]  # in mg per 100g
    calcium: Optional[float]  # in mg per 100g
    magnesium: Optional[float]  # in mg per 100g
    phosphorus: Optional[float]  # in mg per 100g
    iron: Optional[float]  # in mg per 100g
    zinc: Optional[float]  # in mg per 100g
    iodine: Optional[float]  # in µg per 100g
    copper: Optional[float]  # in µg per 100g
    manganese: Optional[float]  # in µg per 100g
    fluoride: Optional[float]  # in µg per 100g
    chromium: Optional[float]  # in µg per 100g
    molybdenum: Optional[float]  # in µg per 100g
    vitamin_a_re: Optional[float]  # in µg per 100g
    vitamin_a_rae: Optional[float]  # in µg per 100g
    retinol: Optional[float]  # in µg per 100g
    beta_carotene: Optional[float]  # in µg per 100g
    vitamin_d: Optional[float]  # in µg per 100g
    vitamin_d2: Optional[float]  # in µg per 100g
    vitamin_d3: Optional[float]  # in µg per 100g
    vitamin_e: Optional[float]  # in mg per 100g
    alpha_tocopherol: Optional[float]  # in mg per 100g
    vitamin_k: Optional[float]  # in µg per 100g
    vitamin_k1: Optional[float]  # in µg per 100g
    vitamin_k2: Optional[float]  # in µg per 100g
    vitamin_b1: Optional[float]  # in mg per 100g
    vitamin_b2: Optional[float]  # in mg per 100g
    niacin: Optional[float]  # in mg per 100g
    niacin_equivalent: Optional[float]  # in mg per 100g
    pantothenic_acid: Optional[float]  # in mg per 100g
    vitamin_b6: Optional[float]  # in µg per 100g
    biotin: Optional[float]  # in µg per 100g
    folate_equivalent: Optional[float]  # in µg per 100g
    folate: Optional[float]  # in µg per 100g
    folic_acid: Optional[float]  # in µg per 100g
    vitamin_b12: Optional[float]  # in µg per 100g
    vitamin_c: Optional[float]  # in mg per 100g

    def __post_init__(self):
        """Validate that the nutrient values are non-negative."""
        _validate_non_negative(
            {
                "water": self.water,
                "monounsaturated_fat": self.monounsaturated_fat,
                "polyunsaturated_fat": self.polyunsaturated_fat,
                "omega_3": self.omega_3,
                "omega_6": self.omega_6,
                "starch": self.starch,
                "alcohol": self.alcohol,
                "sodium": self.sodium,
                "cholesterol": self.cholesterol,
                "potassium": self.potassium,
                "calcium": self.calcium,
                "magnesium": self.magnesium,
                "phosphorus": self.phosphorus,
                "iron": self.iron,
                "zinc": self.zinc,
                "iodine": self.iodine,
                "copper": self.copper,
                "manganese": self.manganese,
                "fluoride": self.fluoride,
                "chromium": self.chromium,
                "molybdenum": self.molybdenum,
                "vitamin_a_re": self.vitamin_a_re,
                "vitamin_a_rae": self.vitamin_a_rae,
                "retinol": self.retinol,
                "beta_carotene": self.beta_carotene,
                "vitamin_d": self.vitamin_d,
                "vitamin_d2": self.vitamin_d2,
                "vitamin_d3": self.vitamin_d3,
                "vitamin_e": self.vitamin_e,
                "alpha_tocopherol": self.alpha_tocopherol,
                "vitamin_k": self.vitamin_k,
                "vitamin_k1": self.vitamin_k1,
                "vitamin_k2": self.vitamin_k2,
                "vitamin_b1": self.vitamin_b1,
                "vitamin_b2": self.vitamin_b2,
                "niacin": self.niacin,
                "niacin_equivalent": self.niacin_equivalent,
                "pantothenic_acid": self.pantothenic_acid,
                "vitamin_b6": self.vitamin_b6,
                "biotin": self.biotin,
                "folate_equivalent": self.folate_equivalent,
                "folate": self.folate,
                "folic_acid": self.folic_acid,
                "vitamin_b12": self.vitamin_b12,
                "vitamin_c": self.vitamin_c,
            }
        )


class Food:
    """This class defines the food-items."""

    def __init__(
        self,
        food_id,
        name,
        unit_type,
        calories,
        big_seven_per_100g: BigSeven,
        nutrient_summary: NutrientSummary,
    ):
        """This is the constructor of Food."""
        self._id = food_id
        self._name = name
        self._unit_type = unit_type
        self._calories_per_100_units = calories
        self._big_seven_per_100_units = big_seven_per_100g
        self._nutrient_summary = nutrient_summary


class Meal:
    """This class defines the meal."""

    def __init__(self, meal_id, name, items: list[Food]):
        """This is the constructor of Meal."""
        self._id = meal_id
        self._name = name
        self._items = items

    # Here are the meal related methods.

    def calculate_calories(self):
        """Method for calculating the calories of the meal."""
        if not self._items:
            return 0
        total_calories = 0
        for item in self._items:
            factor = item.amount_in_gram / 100
            total_calories += item.calories_per_100_units * factor
        return total_calories

    def calculate_big_seven(self):
        """Method for calculating the nutrient summary of the meal."""
        if not self._items:
            return _zero_dataclass(BigSeven)

        total = {
            "calorie": 0,
            "fat": 0,
            "saturated_fat": 0,
            "carbohydrate": 0,
            "fibre": 0,
            "sugar": 0,
            "protein": 0,
            "salt": 0,
        }

        for item in self._items:
            factor = item.amount_in_gram / 100
            nutrients = item.food.nutrients_per_100g
            total["calorie"] += nutrients.calorie * factor
            total["fat"] += nutrients.fat * factor
            total["saturated_fat"] += nutrients.saturated_fat * factor
            total["carbohydrate"] += nutrients.carbohydrate * factor
            total["fibre"] += nutrients.fibre * factor
            total["sugar"] += nutrients.sugar * factor
            total["protein"] += nutrients.protein * factor
            total["salt"] += nutrients.salt * factor

        return BigSeven(
            total["calorie"],
            total["fat"],
            total["saturated_fat"],
            total["carbohydrate"],
            total["fibre"],
            total["sugar"],
            total["protein"],
        )

    def calculate_nutrient_summary(self):
        """Method for calculating the nutrient summary of the meal."""
        if not self._items:
            return _zero_dataclass(NutrientSummary)
        total = {
            "water": 0,
            "monounsaturated_fat": 0,
            "polyunsaturated_fat": 0,
            "omega_3": 0,
            "omega_6": 0,
            "starch": 0,
            "alcohol": 0,
            "sodium": 0,
            "cholesterol": 0,
            "potassium": 0,
            "calcium": 0,
            "magnesium": 0,
            "phosphorus": 0,
            "iron": 0,
            "zinc": 0,
            "iodine": 0,
            "copper": 0,
            "manganese": 0,
            "fluoride": 0,
            "chromium": 0,
            "molybdenum": 0,
            "vitamin_a_re": 0,
            "vitamin_a_rae": 0,
            "retinol": 0,
            "beta_carotene": 0,
            "vitamin_d": 0,
            "vitamin_d2": 0,
            "vitamin_d3": 0,
            "vitamin_e": 0,
            "alpha_tocopherol": 0,
            "vitamin_k": 0,
            "vitamin_k1": 0,
            "vitamin_k2": 0,
            "vitamin_b1": 0,
            "vitamin_b2": 0,
            "niacin": 0,
            "niacin_equivalent": 0,
            "pantothenic_acid": 0,
            "vitamin_b6": 0,
            "biotin": 0,
            "folate_equivalent": 0,
            "folate": 0,
            "folic_acid": 0,
            "vitamin_b12": 0,
            "vitamin_c": 0,
        }
        for item in self._items:
            factor = item.amount_in_gram / 100
            nutrients = item.food.nutrient_summary
            total["water"] += nutrients.water * factor
            total["monounsaturated_fat"] += nutrients.monounsaturated_fat * factor
            total["polyunsaturated_fat"] += nutrients.polyunsaturated_fat * factor
            total["omega_3"] += nutrients.omega_3 * factor
            total["omega_6"] += nutrients.omega_6 * factor
            total["starch"] += nutrients.starch * factor
            total["alcohol"] += nutrients.alcohol * factor
            total["sodium"] += nutrients.sodium * factor
            total["cholesterol"] += nutrients.cholesterol * factor
            total["potassium"] += nutrients.potassium * factor
            total["calcium"] += nutrients.calcium * factor
            total["magnesium"] += nutrients.magnesium * factor
            total["phosphorus"] += nutrients.phosphorus * factor
            total["iron"] += nutrients.iron * factor
            total["zinc"] += nutrients.zinc * factor
            total["iodine"] += nutrients.iodine * factor
            total["copper"] += nutrients.copper * factor
            total["manganese"] += nutrients.manganese * factor
            total["fluoride"] += nutrients.fluoride * factor
            total["chromium"] += nutrients.chromium * factor
            total["molybdenum"] += nutrients.molybdenum * factor
            total["vitamin_a_re"] += nutrients.vitamin_a_re * factor
            total["vitamin_a_rae"] += nutrients.vitamin_a_rae * factor
            total["retinol"] += nutrients.retinol * factor
            total["beta_carotene"] += nutrients.beta_carotene * factor
            total["vitamin_d"] += nutrients.vitamin_d * factor
            total["vitamin_d2"] += nutrients.vitamin_d2 * factor
            total["vitamin_d3"] += nutrients.vitamin_d3 * factor
            total["vitamin_e"] += nutrients.vitamin_e * factor
            total["alpha_tocopherol"] += (
                nutrients.alpha_tocopherol * factor  # noqa: E501, refactored by ai
            )
            total["vitamin_k"] += nutrients.vitamin_k * factor
            total["vitamin_k1"] += nutrients.vitamin_k1 * factor
            total["vitamin_k2"] += nutrients.vitamin_k2 * factor
            total["vitamin_b1"] += nutrients.vitamin_b1 * factor
            total["vitamin_b2"] += nutrients.vitamin_b2 * factor
            total["niacin"] += nutrients.niacin * factor
            total["niacin_equivalent"] += nutrients.niacin_equivalent * factor
            total["pantothenic_acid"] += nutrients.pantothenic_acid * factor
            total["vitamin_b6"] += nutrients.vitamin_b6 * factor
            total["biotin"] += nutrients.biotin * factor
            total["folate_equivalent"] += nutrients.folate_equivalent * factor
            total["folate"] += nutrients.folate * factor
            total["folic_acid"] += nutrients.folic_acid * factor
            total["vitamin_b12"] += nutrients.vitamin_b12 * factor
            total["vitamin_c"] += nutrients.vitamin_c * factor
        return NutrientSummary(
            total["water"],
            total["monounsaturated_fat"],
            total["polyunsaturated_fat"],
            total["omega_3"],
            total["omega_6"],
            total["starch"],
            total["alcohol"],
            total["sodium"],
            total["cholesterol"],
            total["potassium"],
            total["calcium"],
            total["magnesium"],
            total["phosphorus"],
            total["iron"],
            total["zinc"],
            total["iodine"],
            total["copper"],
            total["manganese"],
            total["fluoride"],
            total["chromium"],
            total["molybdenum"],
            total["vitamin_a_re"],
            total["vitamin_a_rae"],
            total["retinol"],
            total["beta_carotene"],
            total["vitamin_d"],
            total["vitamin_d2"],
            total["vitamin_d3"],
            total["vitamin_e"],
            total["alpha_tocopherol"],
            total["vitamin_k"],
            total["vitamin_k1"],
            total["vitamin_k2"],
            total["vitamin_b1"],
            total["vitamin_b2"],
            total["niacin"],
            total["niacin_equivalent"],
            total["pantothenic_acid"],
            total["vitamin_b6"],
            total["biotin"],
            total["folate_equivalent"],
            total["folate"],
            total["folic_acid"],
            total["vitamin_b12"],
            total["vitamin_c"],
        )

    def add_food_composition(self, food_item):
        """Method for adding a meal composition. (Later when DB exists)"""
        self._items.append(food_item)
