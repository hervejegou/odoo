from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.session import Session
from werkzeug.utils import redirect as werkzeug_redirect
import requests
import logging
_logger = logging.getLogger(__name__)

class SessionWebsite(Session):

    @http.route('/web/session/logout', website=True, multilang=False, sitemap=False)
    def logout(self, redirect='/odoo'):
        auth0_provider = request.env['auth.oauth.provider'].sudo().search([('auth0_tenant_domain', '!=', False),('enabled','=', True)], limit=1)
        if auth0_provider:
            auth0_logout_url = auth0_provider.auth0_logout_url
            try:
                response = requests.request("GET", auth0_logout_url, headers={}, data={},timeout=10)
                _logger.error('xxxxxx: %s'%response.text)
                if response.status_code == 200:
                    return werkzeug_redirect(auth0_logout_url, code=303)
            except requests.RequestException as e:
                _logger.error('ERRRORORROROROR: %s' % e)
                return super().logout(redirect=redirect)

        return super().logout(redirect=redirect)



