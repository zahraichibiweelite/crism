# -*- encoding: utf-8 -*-

{
    'name': 'WLTDebrand',
    'summary': 'WLT Back',
    'version': '13.5',
    'category': 'Website',
    'summary': """
Debrand Odoo
""",
    'author': "WEELITE (www.weelite.ma)",
    'website': 'http://www.weelite.ma',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'website',
        'mail'
    ],
    'data': [
        'templates/views.xml',
        'templates/login_page.xml',
    ],
    'installable': True,
    'application': True,
}