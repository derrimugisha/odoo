from odoo import api, fields, models


class DerriHospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "patient recors"
    _inherit = "mail.thread"
    name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    is_child = fields.Boolean(string="is child ?", tracking=True)
    notes = fields.Text(string="Notes", tracking=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender")

    capitalized_name = fields.Char(
        string="Capitalized Name", compute="_compute_capitalized_name")

    @api.depends("name")
    def _compute_capitalized_name(self):
        if self.name:
            self.capitalized_name = self.name.upper()
        else:
            self.capitalized_name = ""

    @api.onchange("age")
    def on_change_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False
