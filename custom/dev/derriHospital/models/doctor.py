from odoo import fields, api, models


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = "mail.thread"
    _description = "Doctor Records"

    name = fields.Char(string="Name", required=True, tracking=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender", tracking=True)
    ref = fields.Char(string="Reference", required=True)
