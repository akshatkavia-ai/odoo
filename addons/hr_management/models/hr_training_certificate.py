from odoo import fields, models


class HrTrainingCertificate(models.Model):
    """Training completion certificate (scaffolding only)."""

    _name = "hr.training.certificate"
    _description = "Training Certificate"

    name = fields.Char(string="Certificate Name", required=True)
    employee_profile_id = fields.Many2one(
        comodel_name="hr.employee.profile",
        string="Employee Profile",
        required=True,
        ondelete="cascade",
    )
    training_session_id = fields.Many2one(
        comodel_name="hr.training.session",
        string="Training Session",
        required=True,
        ondelete="cascade",
    )
    issue_date = fields.Date(string="Issue Date")
    score = fields.Float(string="Score")
    certificate_number = fields.Char(string="Certificate Number")
