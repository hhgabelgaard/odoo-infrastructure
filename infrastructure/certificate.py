# -*- coding: utf-8 -*-
from odoo.exceptions import Warning
from odoo import models, fields


class Certificate(models.Model):
    """"""

    _name = 'infrastructure.certificate'
    _description = 'SSL Certificate'

    name = fields.Char(
        string='Name',
        required=True
    )

    pemfile = fields.Char(
        string='PEM file',
        help="Absolute path to .pem file",
        required=True
    )

    keyfile = fields.Char(
        string='Key file',
        help="Absolute path to .key file",
        required=True
    )

    server_id = fields.Many2one(
        'infrastructure.server',
        string='server',
        ondelete='cascade',
        required=True
    )
    
    instance_host_ids = fields.One2many(
        'infrastructure.instance_host',
        'certificate_id',
        string='Instances/Host',
    )
    
    instance_ids = fields.One2many(
        'infrastructure.instance',
        'certificate_id',
        string='Instances',
    )

