{
    "name": "HR Management (Custom)",
    "version": "19.0.1.0.0",
    "category": "Human Resources",
    "summary": "Custom HR management scaffolding (employee profiles and training).",
    "description": """
Custom HR management scaffolding:
- Employee profile extension model
- Training sessions, enrollments, and certificates

This module intentionally contains scaffolding only (models/fields/views/security).
No business logic, validations, computed fields, or controllers are included.
""",
    "author": "Custom",
    "website": "",
    "license": "LGPL-3",
    "depends": [
        "base",
        "hr",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_views.xml",
        "views/hr_training_views.xml",
    ],
    "application": False,
    "installable": True,
}
