from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.session import Session

class SessionWebsite(Session):

    @http.route('/web/session/logout', website=True, multilang=False, sitemap=False)
    def logout(self, redirect='/odoo'):
        auth0_provider = request.env['auth.oauth.provider'].ref("knk_auth0_sso.auth_oauth_provider_auth0")
        if auth0_provider:
            redirect = auth0_provider.logout_url
        else:
            auth0_provider = request.env['auth.oauth.provider'].sudo().search([('auth0_provider', '=', True)], limit=1)
            redirect = auth0_provider.logout_url or '/odoo'
        return super().logout(redirect=redirect)
