# -*- coding: utf-8 -*-
{
    'name': "website_custom",

    'summary': "Add custom functionality to the website",

    'description': """ """,

    'author': "paneco",
    'website': "https://www.paneco.energy",

    'category': 'website',
    'version': '0.1',
    'license': 'LGPL-3',
    'data': [
        'views/auth_signup_login_template.xml',
        'views/providers_template.xml',
        'views/web_login_template.xml'
    ],
    'depends': ['base','web','auth_oauth','auth_signup']
}

