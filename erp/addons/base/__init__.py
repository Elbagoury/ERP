# -*- coding: utf-8 -*-
# Part of ERP. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import populate
from . import report
from . import wizard


def post_init(cr, registry):
    """Rewrite ICP's to force groups"""
    from erp import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.config_parameter'].init(force=True)
