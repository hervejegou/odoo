from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.session import Session
from werkzeug.utils import redirect as werkzeug_redirect
import requests

class SessionWebsite(Session):

    @http.route('/web/session/logout', website=True, multilang=False, sitemap=False)
    def logout(self, redirect='/odoo'):
        auth0_provider = request.env['auth.oauth.provider'].sudo().search([('auth0_tenant_domain', '!=', False),('enabled','=', True)], limit=1)
        if auth0_provider:
            auth0_logout_url = auth0_provider.auth0_logout_url
            response = requests.request("GET", auth0_logout_url, headers={}, data={},timeout=10)
            if response.status_code == 200:
                return werkzeug_redirect(auth0_logout_url, code=303)
        return super().logout(redirect=redirect)



