# Part of ERP. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models

from erp.http import request


def _post_init_hook(cr, registry):
    if request:
        request.is_frontend = False
        request.is_frontend_multilang = False
