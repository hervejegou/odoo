# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

class IntercomUserData(http.Controller):

    @http.route('/intercom/user_info', type='json',methods=['POST'], auth='user', csrf=False)
    def intercom_user_info(self):
        user = request.env.user
        _logger.info(f"Fetching Intercom user info for user: {user.name} (ID: {user})")
        return {
            'email': user.email,
            'user_id': user.id,
            'name': user.name,
        }

