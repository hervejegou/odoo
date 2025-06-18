# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class IntercomUserData(http.Controller):

    @http.route('/intercom/user_info', type='json', auth='user')
    def intercom_user_info(self):
        user = request.env.user
        return {
            'email': user.email,
            'user_id': user.id,
            'name': user.name,
        }

