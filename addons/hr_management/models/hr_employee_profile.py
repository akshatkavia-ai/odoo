from odoo import fields, models


class HrEmployeeProfile(models.Model):
    """Additional employee profile information (scaffolding only)."""

    _name = "hr.employee.profile"
    _description = "Employee Profile"

    employee_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Employee",
        required=True,
        ondelete="cascade",
        help="Employee to which this profile belongs.",
    )
    work_email = fields.Char(string="Work Email")
    work_phone = fields.Char(string="Work Phone")
    emergency_contact_name = fields.Char(string="Emergency Contact Name")
    emergency_contact_phone = fields.Char(string="Emergency Contact Phone")
    start_date = fields.Date(string="Start Date")
    notes = fields.Char(string="Notes")

    training_enrollment_ids = fields.One2many(
        comodel_name="hr.training.enrollment",
        inverse_name="employee_profile_id",
        string="Training Enrollments",
    )
    certificate_ids = fields.One2many(
        comodel_name="hr.training.certificate",
        inverse_name="employee_profile_id",
        string="Training Certificates",
    )
