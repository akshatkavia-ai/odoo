from odoo import fields, models


class FleetMaintenanceRecord(models.Model):
    """Maintenance record linked to a custom vehicle (scaffolding only)."""

    _name = "fleet.maintenance.record"
    _description = "Maintenance Record (Custom)"

    vehicle_id = fields.Many2one(
        comodel_name="fleet.management.vehicle",
        string="Vehicle",
        required=True,
        ondelete="cascade",
    )
    name = fields.Char(string="Title", required=True)
    maintenance_date = fields.Date(string="Maintenance Date")
    cost = fields.Float(string="Cost")
    vendor = fields.Char(string="Vendor")
    notes = fields.Char(string="Notes")
