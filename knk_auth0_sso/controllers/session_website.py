from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.session import Session

class SessionWebsite(Session):

    @http.route('/web/session/logout', website=True, multilang=False, sitemap=False)
    def logout(self, redirect='/odoo'):
        auth0_provider = request.env['auth.oauth.provider'].sudo().search([('auth0_tenant_domain', '!=', False),('enabled','=', True)], limit=1)

        if auth0_provider:
            redirect = auth0_provider.auth0_logout_url
        else:
            redirect = '/odoo'
        return super().logout(redirect=redirect)
