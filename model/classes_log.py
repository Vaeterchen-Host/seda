# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Tobias Mignat & Sabine Steverding
# See LICENSE.md for the full license text.

"""This module contains the log classes for the application."""

from datetime import datetime


## All classes for logging
# Parent classes.
class LogItem:
    """This is the parent class for all log items."""

    def __init__(self, log_id, log_value, unit_type, timestamp=None):
        """This is the constructor of LogItem."""
        self._log_id = log_id
        self._log_value = log_value
        self._unit_type = unit_type
        self._timestamp = timestamp

        if self._timestamp is None:
            self.create_timestamp()

    @property
    def id(self):
        """This is the getter for 'log_id'."""
        return self._log_id

    @property
    def log_value(self):
        """This is the getter for 'log_value'."""
        return self._log_value

    @property
    def unit_type(self):
        """This is the getter for 'unit_type'."""
        return self._unit_type

    @property
    def timestamp(self):
        """This is the getter for 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, new_timestamp):
        """This is the setter for timestamp. It checks format."""
        if not isinstance(new_timestamp, datetime):
            raise ValueError("Timestamp must be a datetime object.")
        self._timestamp = new_timestamp

    def create_timestamp(self):
        """Method for creating a timestamp. It can be used when creating a new log item."""
        self._timestamp = datetime.now()


class LogHandler:
    """This is the parent class for all log handlers."""

    def __init__(self, user_id, LogItem: list[LogItem]):
        """This is the constructor of LogHandler."""
        self._user_id = user_id
        self._logs = LogItem


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
        """This is the setter for activity log."""
        self._id = new_id
