from odoo import fields, models


class FleetManagementVehicle(models.Model):
    """Vehicle record for custom fleet management (scaffolding only)."""

    _name = "fleet.management.vehicle"
    _description = "Fleet Vehicle (Custom)"

    name = fields.Char(string="Vehicle Name", required=True)
    license_plate = fields.Char(string="License Plate")
    vin_sn = fields.Char(string="VIN")
    acquisition_date = fields.Date(string="Acquisition Date")
    odometer = fields.Float(string="Odometer")
    notes = fields.Char(string="Notes")

    maintenance_record_ids = fields.One2many(
        comodel_name="fleet.maintenance.record",
        inverse_name="vehicle_id",
        string="Maintenance Records",
    )
