{
    "name": "Fleet Management (Custom)",
    "version": "19.0.1.0.0",
    "category": "Fleet",
    "summary": "Custom fleet management scaffolding (vehicles and maintenance records).",
    "description": """
Custom fleet management scaffolding:
- Vehicle model
- Maintenance records linked to vehicles

This module intentionally contains scaffolding only (models/fields/views/security).
No business logic, validations, computed fields, or controllers are included.
""",
    "author": "Custom",
    "website": "",
    "license": "LGPL-3",
    "depends": [
        "base",
        "fleet",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/fleet_vehicle_views.xml",
    ],
    "application": False,
    "installable": True,
}
