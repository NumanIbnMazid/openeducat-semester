# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
# from odoo.api import Environment as env
from .utils import create_or_update_course


class BaseArchive(models.AbstractModel):
    _name = 'base.archive'
    _description = 'Abstract Archive'

    active = fields.Boolean(default=True)

    def do_archive(self):
        for record in self:
            record.active = not record.active

class OpSemester(models.Model):
    _name = 'op.semester'
    _inherit = ['base.archive']
    _description = 'Openeducat Semester'

    name = fields.Char('Title', required=True)
    semester_category_id = fields.Many2one(
        'op.semester.category', string='Semester Category', required=True)
    short_name = fields.Char('Short Title', translate=True, index=True)
    code = fields.Char('Code', size=16, required=True)
    description = fields.Html('Description', sanitize=True, strip_style=False)
    credit = fields.Float('Credit', required=True)
    course_id = fields.Many2one('op.course', string='Course', ondelete='set null')
    subject_ids = fields.Many2many('op.subject', string='Subject(s)')

    _sql_constraints = [
        ('unique_semester_code',
         'unique(code)', 'Code should be unique per semester!')]

    def name_get(self):
        """ This method used to customize display name of the record """
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.semester_category_id.name)
            result.append((record.id, rec_name))
        return result

    @api.model
    def create(self, values):
        record = super(OpSemester, self).create(values)
        create_or_update_course(self=self, values=values, record=record)
        return record

    
    def write(self, values):
        create_or_update_course(self=self, values=values, record=None)
        record = super(OpSemester, self).write(values)
        return record


class OpCourse(models.Model):
    _inherit = 'op.course'

    semester_ids = fields.Many2many('op.semester', 'id', string='Semesters')
