from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.session import Session
from werkzeug.utils import redirect as werkzeug_redirect


class SessionWebsite(Session):

    @http.route('/web/session/logout/auth0', website=True, multilang=False, sitemap=False)
    def logout_auth0(self):
        auth0_provider = request.env['auth.oauth.provider'].sudo().search([('auth0_tenant_domain', '!=', False),('enabled','=', True)], limit=1)
        if auth0_provider:
            auth0_logout_url = auth0_provider.auth0_logout_url
            return werkzeug_redirect(auth0_logout_url, code=303)
        else:
            request.session.logout(keep_db=True)



