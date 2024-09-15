# -*- coding: utf-8 -*-
# Part of ERP. See LICENSE file for full copyright and licensing details.

""" Addons module.

This module serves to contain all ERP addons, across all configured addons
paths. For the code to manage those addons, see erp.modules.

Addons are made available under `erp.addons` after
erp.tools.config.parse_config() is called (so that the addons paths are
known).

This module also conveniently reexports some symbols from erp.modules.
Importing them from here is deprecated.

"""
# make erp.addons a namespace package, while keeping this __init__.py
# present, for python 2 compatibility
# https://packaging.python.org/guides/packaging-namespace-packages/
import pkgutil
import os.path
__path__ = [
    os.path.abspath(path)
    for path in pkgutil.extend_path(__path__, __name__)
]
