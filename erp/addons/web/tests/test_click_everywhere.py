# Part of ERP. See LICENSE file for full copyright and licensing details.

import logging
import erp.tests

_logger = logging.getLogger(__name__)


@erp.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusAdmin(erp.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_everywhere_as_admin(self):
        menus = self.env['ir.ui.menu'].load_menus(False)
        for app_id in menus['root']['children']:
            with self.subTest(app=menus[app_id]['name']):
                _logger.runbot('Testing %s', menus[app_id]['name'])
                self.browser_js("/web", "erp.__DEBUG__.services['web.clickEverywhere']('%s');" % menus[app_id]['xmlid'], "erp.isReady === true", login="admin", timeout=600)
                self.terminate_browser()


@erp.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusDemo(erp.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_everywhere_as_demo(self):
        user_demo = self.env.ref("base.user_demo")
        menus = self.env['ir.ui.menu'].with_user(user_demo.id).load_menus(False)
        for app_id in menus['root']['children']:
            with self.subTest(app=menus[app_id]['name']):
                _logger.runbot('Testing %s', menus[app_id]['name'])
                self.browser_js("/web", "erp.__DEBUG__.services['web.clickEverywhere']('%s');" % menus[app_id]['xmlid'], "erp.isReady === true", login="demo", timeout=600)
                self.terminate_browser()

@erp.tests.tagged('post_install', '-at_install')
class TestMenusAdminLight(erp.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_apps_menus_as_admin(self):
        self.browser_js("/web", "erp.__DEBUG__.services['web.clickEverywhere'](undefined, true);", "erp.isReady === true", login="admin", timeout=120)

@erp.tests.tagged('post_install', '-at_install',)
class TestMenusDemoLight(erp.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_apps_menus_as_demo(self):
        self.browser_js("/web", "erp.__DEBUG__.services['web.clickEverywhere'](undefined, true);", "erp.isReady === true", login="demo", timeout=120)
