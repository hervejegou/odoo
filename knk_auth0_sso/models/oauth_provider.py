# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

import logging
import requests

from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class AuthOauthProvider(models.Model):
    _inherit = "auth.oauth.provider"

    auth0_tenant_domain = fields.Char(string="Auth0 Domain")
    auth0_client_secret = fields.Char(string='Secret Key')
    auth0_provider = fields.Boolean(compute="_compute_auth0_provider")
    auth0_logout_url = fields.Char(string="Auth0 Logout Redirect URL",
                                   default='/odoo',
                                   help="URL to redirect after logout from Auth0. If not set, it will use the default Odoo logout URL.")

    auth_endpoint = fields.Char(string="Authorization Endpoint", compute='_compute_auth0_endpoints', store=True)
    validation_endpoint = fields.Char(string="Token Validation Endpoint", compute='_compute_auth0_endpoints', store=True)
    data_endpoint = fields.Char(string="User Info Endpoint", compute='_compute_auth0_endpoints', store=True)

    @api.depends('auth0_tenant_domain')
    def _compute_auth0_endpoints(self):
        for rec in self:
            domain = rec.auth0_tenant_domain
            if domain:
                rec.auth_endpoint = f'https://{domain}/authorize'
                rec.validation_endpoint = f'https://{domain}/oauth/token'
                rec.data_endpoint = f'https://{domain}/userinfo'
            else:
                rec.auth_endpoint = False
                rec.validation_endpoint = False
                rec.data_endpoint = False

    @api.onchange('data_endpoint')
    def _compute_auth0_provider(self):
        for provider in self:
            provider.auth0_provider = False
            if provider.data_endpoint:
                if "auth0.com/userinfo" in provider.data_endpoint or "/userinfo" in provider.data_endpoint:
                    provider.auth0_provider = True

    def auth0_validate_token(self, access_token):
        headers = {"Authorization": f"Bearer {access_token}"}
        try:
            response = requests.get(self.data_endpoint, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                _logger.error("Auth0 validation failed with status %s: %s", response.status_code, response.text)
        except Exception as e:
            _logger.error("Error validating Auth0 token: %s", e)
        return False

    def get_auth0_oauth_token(self, code=None, refresh_token=None):
        try:
            requests.get("https://auth0.com", timeout=5)
        except (requests.ConnectionError, requests.Timeout) as exception:
            _logger.error("Internet connection issue: %s", str(exception))
            return None

        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        redirect_url = f"{base_url}/auth_oauth/auth0/signin"

        data = {
            "client_id": self.client_id,
            "client_secret": self.auth0_client_secret,
            "redirect_uri": redirect_url,
            "grant_type": "authorization_code" if code else "refresh_token",
        }
        if code:
            data.update({
                "code": code
            })
        elif refresh_token:
            data.update({
                "refresh_token": refresh_token
            })

        headers = {
            "content-type": "application/x-www-form-urlencoded"
        }

        try:
            response = requests.post(self.validation_endpoint, data=data, headers=headers)
            response_data = response.json()

            if response.status_code == 200 and "access_token" in response_data:
                return response_data
            else:
                _logger.error("Failed to retrieve Auth0 OAuth token: %s", response_data)
                return None
        except Exception as e:
            _logger.error("Error while requesting Auth0 OAuth token: %s", e)
            return None
