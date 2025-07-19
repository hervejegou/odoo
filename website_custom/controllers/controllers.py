# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.web.controllers.home import Home as WebHome
from odoo.addons.web.controllers.utils import  is_user_internal
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
        if user.partner_id.category_id:
            if hasattr(user.partner_id.category_id, 'mapped'):
                data['tags'] = ' '.join(user.partner_id.category_id.mapped('name'))
            else:
                data['tags'] = user.partner_id.category_id.name
        else:
            data['tags'] = ''
        return http.Response(
            json.dumps(data),
            content_type='application/json; charset=utf-8'
        )

    @http.route('/auth0/callback', type='http', auth='public', website=True)
    def auth0_signin(self, **kw):
        """Handle the callback from Auth0 after user authentication."""
        _logger.info("Auth0 callback received with parameters: %s", kw)
        _logger.info("SEEESSSSIOOOONNN: %s", request.session)
        return request.redirect('/web')

class Home(WebHome):
    def _login_redirect(self, uid, redirect=None):
        if '/odoo' in redirect and not is_user_internal(uid):
            redirect = '/'
        return super()._login_redirect(uid, redirect=redirect)