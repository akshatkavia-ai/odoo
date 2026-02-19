from odoo import fields, models


class HrTrainingEnrollment(models.Model):
    """Employee enrollment to a training session (scaffolding only)."""

    _name = "hr.training.enrollment"
    _description = "Training Enrollment"

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
    enrollment_date = fields.Date(string="Enrollment Date")
    status = fields.Char(string="Status")
