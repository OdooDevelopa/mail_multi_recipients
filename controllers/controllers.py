# -*- coding: utf-8 -*-
from odoo import http

# class MailMultiRecipients(http.Controller):
#     @http.route('/mail_multi_recipients/mail_multi_recipients/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mail_multi_recipients/mail_multi_recipients/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mail_multi_recipients.listing', {
#             'root': '/mail_multi_recipients/mail_multi_recipients',
#             'objects': http.request.env['mail_multi_recipients.mail_multi_recipients'].search([]),
#         })

#     @http.route('/mail_multi_recipients/mail_multi_recipients/objects/<model("mail_multi_recipients.mail_multi_recipients"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mail_multi_recipients.object', {
#             'object': obj
#         })