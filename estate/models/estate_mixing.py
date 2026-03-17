from odoo import fields, models

class EstateMixin(models.Model):
    _name = "estate.mixing"

    name = fields.Char(required=True)