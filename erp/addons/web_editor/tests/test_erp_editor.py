# -*- coding: utf-8 -*-
# Part of ERP. See LICENSE file for full copyright and licensing details.

import erp.tests

@erp.tests.tagged("post_install", "-at_install")
class TestERPEditor(erp.tests.HttpCase):

    def test_erp_editor_suite(self):
        self.browser_js('/web_editor/tests', "", "", login='admin', timeout=1800)
