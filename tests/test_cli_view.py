# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Tobias Mignat & Sabine Steverding
# See LICENSE.md for the full license text.

"""Tests for the CLI view."""

import builtins
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from model.classes import User
from ui import cli_view


def test_change_user_information_allows_name_change(monkeypatch):
    """Changing user information should also allow changing the name. AI-generated."""
    user = User(
        None,
        "Old Name",
        "2000-02-22",
        185,
        "m",
        "beginner",
        [],
        [],
        [],
        [],
    )
    answers = iter(
        [
            "New Name",
            "2001-03-03",
            "190",
            "d",
            "advanced",
        ]
    )
    monkeypatch.setattr(builtins, "input", lambda prompt: next(answers))

    result = cli_view.change_user_information(user)

    assert result == ("New Name", "2001-03-03", 190, "d", "advanced")
