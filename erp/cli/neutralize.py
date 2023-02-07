# -*- coding: utf-8 -*-
# Part of ERP. See LICENSE file for full copyright and licensing details.

import logging
import optparse
import sys

import erp

from . import Command

_logger = logging.getLogger(__name__)


class Neutralize(Command):
    """neutralize a database"""

    def run(self, args):
        parser = erp.tools.config.parser
        group = optparse.OptionGroup(parser, "Neutralize", "Neutralize the database specified by the `-d` argument.")
        group.add_option("--stdout", action="store_true", dest="to_stdout",
                         help="Output the neutralization SQL instead of applying it")
        parser.add_option_group(group)
        opt = erp.tools.config.parse_config(args)

        dbname = erp.tools.config['db_name']
        if not dbname:
            _logger.error('Neutralize command needs a database name. Use "-d" argument')
            sys.exit(1)

        if not opt.to_stdout:
            _logger.info("Starting %s database neutralization", dbname)

        try:
            with erp.sql_db.db_connect(dbname).cursor() as cursor:
                installed_modules = erp.modules.neutralize.get_installed_modules(cursor)
                queries = erp.modules.neutralize.get_neutralization_queries(installed_modules)
                if opt.to_stdout:
                    # pylint: disable=bad-builtin
                    print('BEGIN;')
                    for query in queries:
                        # pylint: disable=bad-builtin
                        print(query.rstrip(";") + ";")
                    # pylint: disable=bad-builtin
                    print("COMMIT;")
                else:
                    for query in queries:
                        cursor.execute(query)
                    _logger.info("Neutralization finished")
        except Exception:
            _logger.critical("An error occurred during the neutralization. THE DATABASE IS NOT NEUTRALIZED!")
            sys.exit(1)
