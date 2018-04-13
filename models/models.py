# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mail_multi_recipients(models.Model):
    _name = 'mail_multi_recipients.mail_multi_recipients'

    name = fields.Char()
    recipient_ids = fields.Many2many(
        comodel_name="res.partner", relation="mail_multi_recipients_partner_rel",
        column1="recipient_id", column2="partner_id")


    @api.multi
    def send_all_email(self):
        self.ensure_one()
        template_id = self.env.ref("mail_multi_recipients.mail_template_demo").id
        compose_form_id = self.env.ref("mail.email_compose_message_wizard_form").id
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': {
                'default_model': 'mail_multi_recipients.mail_multi_recipients',
                'default_res_id': self.id,
                'default_use_template': bool(template_id),
                'default_template_id': template_id,
                'default_composition_mode': 'comment',
                'mark_so_as_sent': True,
                'custom_layout': "mail_multi_recipients.mail_template_demo"
            },
        }
