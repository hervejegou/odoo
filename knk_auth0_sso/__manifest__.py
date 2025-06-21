# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

{
    "name": "Sign in with Auth0",
    "version": "18.0.1.0",
    'summary': 'Auth0 OAuth2 Login for Odoo | Auth0 Single Sign-On | Secure OAuth2 Integration | Token-Based Authentication | Passwordless Login | Auth0 User Profile Access | Third-Party Login System | Seamless Odoo Authentication | External Identity Provider | OAuth2 Login Flow',
    'description': """
        This module integrates Auth0 OAuth2 login into Odoo, enabling users to authenticate using their
        Auth0-managed credentials. It securely handles the entire OAuth2 flow: redirecting users to Auth0,
        exchanging authorization codes for access tokens, and retrieving user profile information such as
        name and email. If a user already exists in Odoo, they are logged in automatically; otherwise, a
        new user account is created. This module supports configurable Auth0 domains, token-based
        authentication, and single sign-on (SSO) capabilities. It's perfect for portals or internal systems
        that require a secure, user-friendly, and centralized identity provider.
        """,
    "license": "OPL-1",
    "category": "Extra Tools",
    "author": "Kanak Infosystems LLP.",
    "website": "https://www.kanakinfosystems.com",
    "depends": ["auth_oauth"],
    "data": [
        "data/auth_oauth_data.xml",
        "views/auth_oauth_views.xml"
    ],
    'assets': {
        'web.assets_frontend': [
            '/knk_auth0_sso/static/src/css/icon.css',
        ]
    },
    'external_dependencies': {
        'python': ['PyJWT'],
    },
    "images": ["static/description/banner.gif"],
    'installable': True,
    'application': False,
    'auto_install': False,
    "price": 35,
    "currency": "EUR",
}
