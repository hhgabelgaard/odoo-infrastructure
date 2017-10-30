# -*- coding: utf-8 -*-
from odoo.exceptions import Warning
from odoo import models, fields


class db_filter(models.Model):
    """"""

    _name = 'infrastructure.db_filter'
    _description = 'db_filter'

    name = fields.Char(
        string='Name',
        required=True
    )

    rule = fields.Char(
        string='Rule',
        required=True
    )
