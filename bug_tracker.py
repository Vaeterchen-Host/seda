"""Known bugs and technical debt for SEDA."""

# pylint: skip-file

BUGS = [
    {
        "id": "BUG-001",
        "title": "Timestamp input in CLI is awkward",
        "status": "open",
        "priority": "medium",
        "area": "ui/cli_view.py",
        "notes": "User currently has to enter ISO format manually.",
    },
    {
        "id": "BUG-002",
        "title": "Height input validation is inconsistent",
        "status": "open",
        "priority": "medium",
        "area": "ui/cli_view.py",
        "notes": "Validation and error messages around height input still need cleanup.",
    },
    {
        "id": "BUG-003",
        "title": "controller.main mixes setup, DB loading and menu control",
        "status": "open",
        "priority": "low",
        "area": "model/controller.py",
        "notes": "Pylint reports too many statements, branches and local variables in main(). Not urgent, but worth refactoring later.",
    },
    {
        "id": "BUG-004",
        "title": "create_user_instance_from_db depends on loop variable db_user",
        "status": "open",
        "priority": "medium",
        "area": "model/controller.py",
        "notes": "The function reads db_user from outer scope. This is fragile and depends on previous control flow."
        "Currently i don't care because of the single-user setup, but this will need to be addressed for multi-user support.",
    },
    {
        "id": "BUG-005",
        "title": "Water and weight logs are loaded without filtering by user",
        "status": "open",
        "priority": "low",
        "area": "model/controller.py",
        "notes": "create_water_log_instances_for_user() and create_weight_log_instances_for_user() currently load every log from the database."
        " This is not a problem with the current single-user setup, but will need to be addressed for multi-user support.",
    },
    {
        "id": "BUG-006",
        "title": "Controller and view naming is still inconsistent",
        "status": "open",
        "priority": "medium",
        "area": "model/controller.py / ui/cli_view.py",
        "notes": "There are several similar names such as show_user_info_from_class, create_water_log_parameters_by_input and older variants. This makes wiring easy to break.",
    },
    {
        "id": "BUG-007",
        "title": "BMI calculator has not implemented the age, yet.",
        "status": "open",
        "priority": "high",
        "area": "model/classes.py",
        "notes": "User.calculate_bmi() already exists.",
    },
    {
        "id": "BUG-008",
        "title": "Daily water intake calculator missing",
        "status": "idea",
        "priority": "high",
        "area": "future feature",
        "notes": "This is more of a future feature than a bug.",
    },
]
