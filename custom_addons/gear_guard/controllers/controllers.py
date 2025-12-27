# -*- coding: utf-8 -*-
# from odoo import http


# class GearGuard(http.Controller):
#     @http.route('/gear_guard/gear_guard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gear_guard/gear_guard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gear_guard.listing', {
#             'root': '/gear_guard/gear_guard',
#             'objects': http.request.env['gear_guard.gear_guard'].search([]),
#         })

#     @http.route('/gear_guard/gear_guard/objects/<model("gear_guard.gear_guard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gear_guard.object', {
#             'object': obj
#         })

