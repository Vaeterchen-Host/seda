# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Tobias Mignat & Sabine Steverding
# See LICENSE.md for the full license text.

"""Main entry point for SEDA."""

import sys
import model.controller
from ui.ui import main, ft

if __name__ == "__main__":
    ux = input("Do you want to run the GUI? (y/n) ").lower()
    if ux == "y":
        ft.app(target=main)
    elif ux == "n":
        model.controller.main()
    else:
        print("Input invalid. Please enter 'y/n'. Exiting now...")
        sys.exit(1)
