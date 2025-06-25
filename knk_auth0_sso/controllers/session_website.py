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
        res = super().logout(redirect=redirect)
        auth0_provider = request.env['auth.oauth.provider'].sudo().search([('auth0_tenant_domain', '!=', False),('enabled','=', True)], limit=1)
        _logger.error("SESSSSSSSSSSSion: %s", request.session.uid)
        if auth0_provider and request.session.uid:
            auth0_logout_url = auth0_provider.auth0_logout_url
            return werkzeug_redirect(auth0_logout_url, code=303)
        return res



