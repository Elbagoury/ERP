# -*- coding: utf-8 -*-
# Part of ERP. See LICENSE file for full copyright and licensing details.

import erp


def get_installed_modules(cursor):
    cursor.execute('''
        SELECT name
          FROM ir_module_module
         WHERE state IN ('installed', 'to upgrade', 'to remove');
    ''')
    return [result[0] for result in cursor.fetchall()]

def get_neutralization_queries(modules):
    # neutralization for each module
    for module in modules:
        filename = erp.modules.get_module_resource(module, 'data/neutralize.sql')
        if filename:
            with erp.tools.misc.file_open(filename) as file:
                yield file.read().strip()
