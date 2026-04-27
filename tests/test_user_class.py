# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Tobias Mignat & Sabine Steverding
# See LICENSE.md for the full license text.

"""Tests for the SEDA user class. Refactored by ai."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from model.class_user import User
from model.classes_log import MealLog, WaterLog, WeightLog

# pylint: skip-file


@pytest.fixture
def water_log_1():
    """Create a waterlog object for each test. Refactored by ai."""
    return WaterLog(1, 1, 900, "2026-03-21T12:12")


@pytest.fixture
def weight_log_1():
    """Create a weightlog object for each test. Refactored by ai."""
    return WeightLog(1, 1, 80.5, "2026-03-21T12:12")


@pytest.fixture
def test_user_class(water_log_1, weight_log_1):
    """Create a fresh user object for each test. Refactored by ai."""
    return User(
        1,
        "Test",
        "2000-02-22",
        185,
        "m",
        "beginner",
        [water_log_1],
        [weight_log_1],
        [],
        [],
    )


def test_get_water_logs(test_user_class):
    """This test checks if water logs are retrieved correctly. Refactored by ai."""
    assert len(test_user_class.water_logs) == 1
    assert test_user_class.water_logs[0].amount_in_ml == 900
    assert test_user_class.water_logs[0].unit_type == "ml"
    assert test_user_class.water_logs[0].timestamp == "2026-03-21T12:12"


def test_add_water_log(test_user_class):
    """This test checks if water logs are added correctly. Refactored by ai."""
    test_user_class.water_log_handler.create_log(
        None, 500, "2026-03-22T08:00"
    )  # refactored by ai

    assert len(test_user_class.water_logs) == 2
    assert test_user_class.water_logs[1].amount_in_ml == 500
    assert test_user_class.water_logs[1].unit_type == "ml"
    assert test_user_class.water_logs[1].timestamp == "2026-03-22T08:00"


def test_get_weight_logs(test_user_class):
    """This test checks if weight logs are retrieved correctly. Refactored by ai."""
    assert len(test_user_class.weight_logs) == 1
    assert test_user_class.weight_logs[0].weight_in_kg == 80.5
    assert test_user_class.weight_logs[0].unit_type == "kg"
    assert test_user_class.weight_logs[0].timestamp == "2026-03-21T12:12"


def test_add_weight_log(test_user_class):
    """This test checks if weight logs are added correctly. Refactored by ai."""
    test_user_class.weight_log_handler.create_log(
        None, 79.8, "2026-03-22T08:00", test_user_class.height_in_cm
    )  # refactored by ai

    assert len(test_user_class.weight_logs) == 2
    assert test_user_class.weight_logs[1].weight_in_kg == 79.8
    assert test_user_class.weight_logs[1].height_in_cm == 185
    assert test_user_class.weight_logs[1].unit_type == "kg"
    assert test_user_class.weight_logs[1].timestamp == "2026-03-22T08:00"


def test_add_activity_log(test_user_class):
    """This test checks if activity logs are added correctly. Refactored by ai."""
    test_user_class.activity_log_handler.create_log(
        None, "walking", 120, "2026-03-22T08:00", 30, "minutes"
    )  # refactored by ai

    assert len(test_user_class.activity_logs) == 1
    assert test_user_class.activity_logs[0].activity_name == "walking"
    assert test_user_class.activity_logs[0].calories_burned == 120
    assert test_user_class.activity_logs[0].activity_value == 30
    assert test_user_class.activity_logs[0].unit_type == "minutes"


def test_set_meal_logs(test_user_class):
    """This test checks if meal logs can be set correctly. Refactored by ai."""
    meal_log = MealLog(1, 1, None, 250, "2026-03-22T12:00")
    test_user_class.meal_logs = [meal_log]

    assert len(test_user_class.meal_logs) == 1
    assert test_user_class.meal_logs[0].id == 1


def test_set_invalid_meal_logs_raises_value_error(test_user_class):
    """This test checks if invalid meal logs are rejected. Refactored by ai."""
    with pytest.raises(ValueError):
        test_user_class.meal_logs = ["not a meal log"]
