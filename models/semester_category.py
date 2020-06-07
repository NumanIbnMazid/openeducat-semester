# -*- coding: utf-8 -*-
from odoo import models, fields, api


class OpSemesterCategory(models.Model):
    _name = 'op.semester.category'
    _description = 'Openeducat Semester Category'

    name = fields.Char('Title', required=True)
    description = fields.Html('Description', sanitize=True, strip_style=False)

    _sql_constraints = [
        ('unique_semester_category_name',
        'unique(name)', 'Semester Category Title must be unique.')
    ]
