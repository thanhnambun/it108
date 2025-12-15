from odoo import models, fields


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    bio = fields.Text(string='Bio')
    is_active = fields.Boolean(string='Is Active', default=True)
