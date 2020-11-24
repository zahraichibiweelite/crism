from odoo.addons.website.controllers.main import Website
from odoo.addons.web.controllers.main import Home
from odoo import http

class HomePage(Website):
    @http.route('/', type='http', auth="none")
    def index(self, s_action=None, db=None, **kw):
        return http.local_redirect('/web', keep_hash=True)

class LoginHome(Home):
    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        return super(LoginHome, self).web_login(redirect, **kw)