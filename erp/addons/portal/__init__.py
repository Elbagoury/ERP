# -*- coding: utf-8 -*-
# Part of ERP. See LICENSE file for full copyright and licensing details.

# Updating mako environement in order to be able to use slug
try:
    from erp.tools.rendering_tools import template_env_globals
    from erp.addons.http_routing.models.ir_http import slug

    template_env_globals.update({
        'slug': slug
    })
except ImportError:
    pass

from . import controllers
from . import models
from . import wizard
