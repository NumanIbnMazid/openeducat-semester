# -*- coding: utf-8 -*-
# from odoo import http


# class OpeneducatSemester(http.Controller):
#     @http.route('/openeducat_semester/openeducat_semester/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openeducat_semester/openeducat_semester/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openeducat_semester.listing', {
#             'root': '/openeducat_semester/openeducat_semester',
#             'objects': http.request.env['openeducat_semester.openeducat_semester'].search([]),
#         })

#     @http.route('/openeducat_semester/openeducat_semester/objects/<model("openeducat_semester.openeducat_semester"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openeducat_semester.object', {
#             'object': obj
#         })
