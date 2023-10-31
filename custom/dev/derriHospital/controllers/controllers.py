from odoo import http
from odoo.http import request
import json


class ApiCall(http.Controller):
    @http.route('/hospital/patients/', auth='odoo')
    def hospital_patient(self, **kw):
        context = {
            'session_info': json.dumps(request.env['ir.http'].session_info())
        }
        # todo.index is the xml template that contains
        # main html content
        # return request.render('todo.index', qcontext=context)
        return "Hello, world!"