# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.interfaces import constrains
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

import json
import logging


logger = logging.getLogger(__name__)
PROFILE_ID = 'profile-ploneconf.site:default'

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
                        "text": "Plone is a CMS built on Python with over 19 years of experience. Plone has a plethora of features that appeal to developers and users alike, such as customizable content types, hierarchical URL object traversing and a sophisticated content workflow powered by a granular permissions model. This allows you to build anything from simple websites to enterprise-grade intranets. Volto exposes all these features and communicates with Plone via its mature REST API. Volto can be esily themed and is highly customizable.",
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
            'ploneconf.site:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    create_volto_homepage()
    portal = api.portal.get()
    set_up_content(portal)


def create_volto_homepage(default_home=HOMEPAGE):
    portal = api.portal.get()
    blocks = default_home['blocks']
    blocks_layout = default_home['blocks_layout']

    portal.setTitle(default_home['title'])
    portal.setDescription(default_home['description'])

    if not getattr(portal, 'blocks', False):
        portal.manage_addProperty('blocks', json.dumps(blocks), 'string')

    if not getattr(portal, 'blocks_layout', False):
        portal.manage_addProperty(
            'blocks_layout', json.dumps(blocks_layout), 'string'
        )


def set_up_content(portal):
    """Create and configure some initial content.
    Part of this code is taken from upgrades.py
    """
    # Create the expected folder-structure
    if 'training' not in portal:
        api.content.create(
            container=portal,
            type='Document',
            id='training',
            title=u'Training')

    if 'schedule' not in portal:
        schedule_folder = api.content.create(
            container=portal,
            type='Document',
            id='schedule',
            title=u'Schedule')
    else:
        schedule_folder = portal['schedule']

    if 'location' not in portal:
        api.content.create(
            container=portal,
            type='Document',
            id='location',
            title=u'Location')

    if 'sponsors' not in portal:
        api.content.create(
            container=portal,
            type='Document',
            id='sponsors',
            title=u'Sponsors')

    if 'sprint' not in portal:
        api.content.create(
            container=portal,
            type='Document',
            id='sprint',
            title=u'Sprint')

    # Allow logged-in users to create content
    api.group.grant_roles(
        groupname='AuthenticatedUsers',
        roles=['Contributor'],
        obj=schedule_folder)

    # Constrain addable types to talk
    behavior = constrains.ISelectableConstrainTypes(schedule_folder)
    behavior.setConstrainTypesMode(constrains.ENABLED)
    behavior.setLocallyAllowedTypes(['talk'])
    behavior.setImmediatelyAddableTypes(['talk'])
    logger.info('Added and configured {0}'.format(schedule_folder.absolute_url()))


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
