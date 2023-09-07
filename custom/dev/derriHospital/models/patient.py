from odoo import api, fields, models
from odoo.exceptions import ValidationError


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
    ref = fields.Char(strinf="Reference", default=lambda self: ("New"))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals["ref"] = self.env["ir.sequence"].next_by_code(
                "hospital.patient")
        return super(DerriHospitalPatient, self).create(vals_list)

    @api.constrains("is_child", "age")
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(("Age can't be Zero"))

    @api.depends("name")
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                self.capitalized_name = self.name.upper()
            else:
                rec.capitalized_name = ""

    @api.onchange("age")
    def on_change_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False
