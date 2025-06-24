from odoo import http
from odoo.addons.web.controllers.session import Session
import requests

class SessionWebsite(Session):

    @http.route('/web/session/logout', website=True, multilang=False, sitemap=False)
    def logout(self, redirect='/odoo'):
        url = "https://skytalk.eu.auth0.com/v2/logout?returnTo=https%3A%2F%2Fwww.paneco.energy%2Fweb%2Fsession%2Flogout%3Fredirect%3D%2F"
        payload = {}
        headers = {}
        requests.request("GET", url, headers=headers, data=payload)
        return super().logout(redirect=redirect)
