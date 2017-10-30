 #-*- coding: utf-8 -*-

from odoo import models, fields


class project_issue(models.Model):

    _inherit = "project.issue"

    database_id = fields.Many2one(
        'infrastructure.database',
        string='Database'
    )
