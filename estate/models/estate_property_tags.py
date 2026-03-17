from odoo import models, fields, api

class EstatePropertyTags(models.Model):
    _name = "estate.property.tags"
    _inherit = "estate.mixing"
    _description = "Tags for Real Estate Models"
    _sql_constraints = [("unique_tag_name", "unique(name)", "Tag Name should be unique")]
    _order = "name desc"

    name = fields.Char(required=True)
    color = fields.Integer(string="Color")


