# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from ploneconf.site.testing import PLONECONF_SITE_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that ploneconf.site is properly installed."""

    layer = PLONECONF_SITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneconf.site is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'ploneconf.site'))

    def test_browserlayer(self):
        """Test that IPloneconfSiteLayer is registered."""
        from ploneconf.site.interfaces import (
            IPloneconfSiteLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPloneconfSiteLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONECONF_SITE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('ploneconf.site')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if ploneconf.site is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'ploneconf.site'))

    def test_browserlayer_removed(self):
        """Test that IPloneconfSiteLayer is removed."""
        from ploneconf.site.interfaces import \
            IPloneconfSiteLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPloneconfSiteLayer, utils.registered_layers())
