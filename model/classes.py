# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Tobias Mignat & Sabine Steverding
# See LICENSE.md for the full license text.

"""Core domain classes for SEDA."""

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


## All classes for logging
# Parent classes.


class MealLog:
    """This class defines the meal log."""

    def __init__(self, meal_log_id, meal, amount_in_gram, timestamp):
        """This is the constructor of MealLog."""
        self._id = meal_log_id
        self._meal = meal
        self._amount_in_gram = amount_in_gram
        self._timestamp = timestamp

    # Here are the meal log related methods.
    @property
    def id(self):
        """This is the getter for id."""
        return self._id

    @id.setter
    def id(self, new_id):
        """This is the setter for id."""
        self._id = new_id

    def calculate_nutrient_summary(self):
        """Method for calculating the nutrient summary of the meal log."""
        meal_summary = self._meal.calculate_nutrient_summary()
        factor = self._amount_in_gram / 100
        return BigSeven(
            fat=meal_summary.fat * factor,
            saturated_fat=meal_summary.saturated_fat * factor,
            carbohydrate=meal_summary.carbohydrate * factor,
            fibre=meal_summary.fibre * factor,
            sugar=meal_summary.sugar * factor,
            protein=meal_summary.protein * factor,
            salt=meal_summary.salt * factor,
        )


class WaterLog:
    """This class defines the water log."""

    def __init__(self, water_log_id, amount_in_ml, timestamp):
        """This is the constructor of WaterLog."""
        self._id = water_log_id
        self.amount_in_ml = amount_in_ml  # refactored by ai
        self.timestamp = timestamp  # refactored by ai

    # Here are the water log related methods.
    @property
    def id(self):
        """This is the getter for id."""
        return self._id

    @id.setter
    def id(self, new_id):
        """This is the setter for id."""
        self._id = new_id

    @property
    def amount_in_ml(self):
        """This is the getter for amount_in_ml."""
        return self._amount_in_ml

    @amount_in_ml.setter
    def amount_in_ml(self, new_amount):
        """This is the setter for amount_in_ml."""
        int(new_amount)
        if new_amount <= 0 or new_amount >= 2000:
            raise ValueError("Amount must be greater than 0 ml.")
        self._amount_in_ml = new_amount

    @property
    def timestamp(self):
        """This is the getter for timestamp."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, new_timestamp):
        """This is the setter for timestamp."""
        self._timestamp = new_timestamp

    # Here are the weight log related methods


class WeightLog:
    """This class defines weightlog."""

    def __init__(self, weight_log_id, weight_in_kg, timestamp):
        """This is the constructor of weightlog."""
        self._id = weight_log_id
        self.weight_in_kg = weight_in_kg  # refactored by ai
        self.timestamp = timestamp  # refactored by ai

    @property
    def id(self):
        """This is the getter for id."""
        return self._id

    @id.setter
    def id(self, new_id):
        """This is the setter for id."""
        self._id = new_id

    @property
    def weight_in_kg(self):
        """This is the getter for weight_in_kg."""
        return self._weight_in_kg

    @weight_in_kg.setter
    def weight_in_kg(self, new_weight):
        """This is the setter for weight_in_kg."""
        if new_weight <= 0 or new_weight > 350:
            raise ValueError("Weight must be between 0 and 350 kg.")
        self._weight_in_kg = new_weight

    @property
    def timestamp(self):
        """This is the getter for timestamp."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, new_timestamp):
        """This is the setter for timestamp."""
        self._timestamp = new_timestamp


class ActivityLog:
    """This class defines the activity log for burned calories."""

    def __init__(self, activity_log_id, activity_name, calories_burned, timestamp):
        """This is the constructor of ActivityLog."""
        self._id = activity_log_id
        self.activity_name = activity_name
        self.calories_burned = calories_burned
        self.timestamp = timestamp

    @property
    def id(self):
        """This is the getter for activity log."""
        return self._id

    @id.setter
    def id(self, new_id):
        """This is the setter vor activity log."""
        self._id = new_id


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
        meal: list[MealLog],
        activity: list[ActivityLog],
    ):
        """This is the constructor of User."""
        self._id = user_id
        self.name = name  # refactored by ai
        self.birthdate = birthdate  # refactored by ai
        self.height_in_cm = height_in_cm  # refactored by ai
        self.gender = gender  # refactored by ai
        self.fitness_lvl = fitness_lvl  # refactored by ai
        self.water_logs = water  # refactored by ai
        self.weight_logs = weight  # refactored by ai
        self.food_logs = food  # refactored by ai
        self.meal_logs = meal  # refactored by ai
        self.activity_logs = activity  # refactored by ai

    # Here are the biometrical data related methods.
    @property
    def id(self):
        """This is the getter for id"""
        return self._id

    @id.setter
    def id(self, new_id):
        """This is the setter for id."""
        self._id = new_id

    @property
    def name(self):
        """This is the getter for name."""
        return self._name

    @name.setter
    def name(self, new_name):
        """This is the setter for name."""
        if not new_name:
            raise ValueError("Name must not be empty.")
        self._name = new_name

    @property
    def birthdate(self):
        """This is the getter for birthdate."""
        return self._birthdate

    @birthdate.setter
    def birthdate(self, new_birthdate):
        """This is the setter for birthdate."""
        self._birthdate = new_birthdate

    @property
    def height_in_cm(self):
        """This is the getter for height_in_cm."""
        return self._height_in_cm

    @height_in_cm.setter
    def height_in_cm(self, new_height):
        """This is the setter for height_in_cm."""
        if new_height <= 0 or new_height > 250:
            raise ValueError("Height must be between 0 and 250 cm.")
        self._height_in_cm = new_height

    @property
    def gender(self):
        """This is the getter for gender."""
        return self._gender

    @gender.setter
    def gender(self, new_gender):
        """This is the setter for gender."""
        if new_gender not in ("m", "f", "d"):
            raise ValueError("Gender must be 'm', 'f' or 'd'.")
        self._gender = new_gender

    @property
    def fitness_lvl(self):
        """This is the getter for fitness_lvl."""
        return self._fitness_lvl

    @fitness_lvl.setter
    def fitness_lvl(self, new_fitness_lvl):
        """This is the setter for fitness_lvl."""
        if new_fitness_lvl not in ("beginner", "intermediate", "advanced"):
            raise ValueError(
                "Fitness level must be 'beginner', 'intermediate' or 'advanced'."
            )
        self._fitness_lvl = new_fitness_lvl

    @property
    def water_logs(self):
        """This is the getter for water logs."""
        return self._water

    @water_logs.setter
    def water_logs(self, new_water_logs):
        """This is the setter for water logs. Partly AI-generated."""
        self._water = _validate_log_list(
            new_water_logs, WaterLog, "Water logs"
        )  # refactored by ai

    @property
    def weight_logs(self):
        """This is the getter for weight logs."""
        return self._weight

    @weight_logs.setter
    def weight_logs(self, new_weight_logs):
        """This is the setter for weight logs. Partly AI-generated."""
        self._weight = _validate_log_list(new_weight_logs, WeightLog, "Weight logs")

    @property
    def food_logs(self):
        """This is the getter for food logs."""
        return self._food

    @food_logs.setter
    def food_logs(self, new_food_logs):
        """This is the setter for food logs. Partly AI-generated."""
        self._food = _validate_log_list(new_food_logs, "Food logs")  # refactored by ai

    @property
    def meal_logs(self):
        """This is the getter for meal logs."""
        return self._meal

    @meal_logs.setter
    def meal_logs(self, new_meal_logs):
        """This is the setter for meal logs. Partly AI-generated."""
        self._meal = _validate_log_list(
            new_meal_logs, MealLog, "Meal logs"
        )  # refactored by ai

    @property
    def activity_logs(self):
        """This is the getter for activity logs."""
        return self._activity

    @activity_logs.setter
    def activity_logs(self, new_activity_logs):
        """This is the setter for activity logs."""
        self._activity = _validate_log_list(
            new_activity_logs, ActivityLog, "Activity logs"
        )  # refactored by ai

    def update_biometrical_data(
        self, birthdate=None, height_in_cm=None, gender=None, fitness_lvl=None
    ):
        """This method updates the biometrical data of the user."""
        if birthdate is not None:
            self.birthdate = birthdate
        if height_in_cm is not None:
            self.height_in_cm = height_in_cm
        if gender is not None:
            self.gender = gender
        if fitness_lvl is not None:
            self.fitness_lvl = fitness_lvl

    # Here are the weight log related methods.
    def add_weight_log(self, weight_in_kg, timestamp=None):
        """Method for adding a weightlog."""
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        new_weight_log = WeightLog(None, weight_in_kg, timestamp)
        self._weight.append(new_weight_log)

    def delete_weight_log(self, weight_log_id):
        """Method for deleting a weightlog within the class instance. AI-generated."""
        remaining_weight_logs = []

        for weight_log in self._weight:
            if weight_log.id != weight_log_id:
                remaining_weight_logs.append(weight_log)

        self._weight = remaining_weight_logs

    def show_weight_logs(self):
        """Method for showing all weightlogs. Partly AI-generated."""
        if not self._weight:
            print("No weight logs found.")
            return
        for log in self._weight:
            print(
                f"ID: {log.id}, Weight: {log.weight_in_kg} kg, Timestamp: {log.timestamp}"
            )

    def calculate_bmi(self):
        """Method for calculating the BMI. Partly AI-generated."""
        if self.height_in_cm is None or not self._weight:
            return "BMI cannot be calculated. Please add a weight log first."
        height_in_m = self.height_in_cm / 100
        latest_weight = self._weight[-1].weight_in_kg
        bmi = latest_weight / (height_in_m**2)
        return round(bmi, 2)

    # Here are the water log related methods.
    def add_water_log(self, amount_in_ml, timestamp=None):
        """Method for adding a waterlog."""
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        new_water_log = WaterLog(None, amount_in_ml, timestamp)
        self._water.append(new_water_log)

    def show_water_logs(self):
        """Method for showing all waterlogs. Partly AI-generated."""
        if not self._water:
            print("No water logs found.")
            return
        for log in self._water:
            print(
                f"ID: {log.id}, Amount: {log.amount_in_ml} ml, Timestamp: {log.timestamp}"
            )

    def delete_water_log(self, water_log_id):
        """Method for deleting a waterlog. AI-generated."""
        remaining_water_logs = []

        for water_log in self._water:
            if water_log.id != water_log_id:
                remaining_water_logs.append(water_log)

        self._water = remaining_water_logs

    def water_intake_today(self):
        """Method for calculating the total water intake of today. Partly AI-generated."""
        today = datetime.now().date()
        total_intake = sum(
            log.amount_in_ml
            for log in self._water
            if datetime.fromisoformat(log.timestamp).date() == today
        )
        return total_intake

    # Here are the food log related methods.
    def add_food_log(self, food_log_id, food, amount_in_gram, timestamp=None):
        """Method for adding a foodlog."""
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        new_food_log = FoodLog(food_log_id, food, amount_in_gram, timestamp)
        self._food.append(new_food_log)

    def delete_food_log(self, food_log_id):
        """Method for deleting a foodlog. AI-generated."""
        remaining_food_logs = []

        for food_log in self._food:
            if food_log.id != food_log_id:
                remaining_food_logs.append(food_log)

        self._food = remaining_food_logs

    # Here are the meal log related methods.
    def add_meal_log(self, meal_log_id, meal, amount_in_gram, timestamp=None):
        """Method for adding a meallog."""
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        new_meal_log = MealLog(meal_log_id, meal, amount_in_gram, timestamp)
        self._meal.append(new_meal_log)

    def delete_meal_log(self, meal_log_id):
        """Method for deleting a meallog. AI-generated."""
        remaining_meal_logs = []

        for meal_log in self._meal:
            if meal_log.id != meal_log_id:
                remaining_meal_logs.append(meal_log)

        self._meal = remaining_meal_logs

    # Here are the activity log related methods.
    def add_activity_log(self, activity_name, calories_burned, timestamp=None):
        """Method for adding an activity log."""
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        new_activity_log = ActivityLog(None, activity_name, calories_burned, timestamp)
        self._activity.append(new_activity_log)

    def delete_activity_log(self, activity_log_id):
        """Method for deleting an activity log. AI-generated."""
        self._activity = [log for log in self._activity if log.id != activity_log_id]
