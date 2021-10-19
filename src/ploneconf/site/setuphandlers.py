# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

import json
import logging

logger = logging.getLogger("ploneconf.site")


HOMEPAGE = {
    "title": "Plone Conference 2035!",
    "description": "The digital experience conference",
    "blocks": {
        "15068807-cfc9-444a-97db-8c736809ff51": {"@type": "title"},
        "59d41d8a-ef05-4e21-8820-2a64f5878098": {
            "@type": "text",
            "text": {
                "blocks": [
                    {
                        "key": "618bl",
                        "text": "Plone is a CMS built on Python with over 20 years of experience. Plone has a plethora of features that appeal to developers and users alike, such as customizable content types, hierarchical URL object traversing and a sophisticated content workflow powered by a granular permissions model. This allows you to build anything from simple websites to enterprise-grade intranets. Volto exposes all these features and communicates with Plone via its mature REST API. Volto can be esily themed and is highly customizable.",
                        "type": "unstyled",
                        "depth": 0,
                        "inlineStyleRanges": [],
                        "entityRanges": [],
                        "data": {},
                    }
                ],
                "entityMap": {},
            },
        },
    },
    "blocks_layout": {
        "items": [
            "15068807-cfc9-444a-97db-8c736809ff51",
            "59d41d8a-ef05-4e21-8820-2a64f5878098",
        ]
    },
}


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "ploneconf.site:uninstall",
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    create_volto_homepage(HOMEPAGE)


def create_volto_homepage(default_home=HOMEPAGE):
    portal = api.portal.get()
    blocks = default_home["blocks"]
    blocks_layout = default_home["blocks_layout"]

    portal.setTitle(default_home["title"])
    portal.setDescription(default_home["description"])

    if not getattr(portal, "blocks", False):
        portal.manage_addProperty("blocks", json.dumps(blocks), "string")

    if not getattr(portal, "blocks_layout", False):
        portal.manage_addProperty("blocks_layout", json.dumps(blocks_layout), "string")


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
