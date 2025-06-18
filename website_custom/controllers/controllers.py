# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging
import json
_logger = logging.getLogger(__name__)

class IntercomUserData(http.Controller):

    @http.route('/intercom/user_info', type='http', methods=['GET'], auth='public', csrf=False)
    def intercom_user_info(self):
        user = request.env.user
        data= {
            'email': user.email,
            'user_id': user.id,
            'name': user.name,
        }
        return http.Response(
            json.dumps(data),
            content_type='application/json; charset=utf-8'
        )

