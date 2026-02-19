from odoo import fields, models


class HrTrainingSession(models.Model):
    """Training session (scaffolding only)."""

    _name = "hr.training.session"
    _description = "Training Session"

    name = fields.Char(string="Title", required=True)
    description = fields.Char(string="Description")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    duration_hours = fields.Float(string="Duration (Hours)")
    trainer_name = fields.Char(string="Trainer")

    enrollment_ids = fields.One2many(
        comodel_name="hr.training.enrollment",
        inverse_name="training_session_id",
        string="Enrollments",
    )
    certificate_ids = fields.One2many(
        comodel_name="hr.training.certificate",
        inverse_name="training_session_id",
        string="Certificates",
    )
