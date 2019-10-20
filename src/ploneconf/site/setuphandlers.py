# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.interfaces import constrains
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

import logging

logger = logging.getLogger(__name__)
PROFILE_ID = 'profile-ploneconf.site:default'


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
    portal = api.portal.get()
    set_up_content(portal)


def set_up_content(portal):
    """Create and configure some initial content.
    Part of this code is taken from upgrades.py
    """
    # Create a folder 'The event' if needed
    if 'the-event' not in portal:
        event_folder = api.content.create(
            container=portal,
            type='Folder',
            id='the-event',
            title=u'The event')
    else:
        event_folder = portal['the-event']

    # Create folder 'Talks' inside 'The event' if needed
    if 'talks' not in event_folder:
        talks_folder = api.content.create(
            container=event_folder,
            type='Folder',
            id='talks',
            title=u'Talks')
    else:
        talks_folder = event_folder['talks']

    # Allow logged-in users to create content
    api.group.grant_roles(
        groupname='AuthenticatedUsers',
        roles=['Contributor'],
        obj=talks_folder)

    # Constrain addable types to talk
    behavior = constrains.ISelectableConstrainTypes(talks_folder)
    behavior.setConstrainTypesMode(constrains.ENABLED)
    behavior.setLocallyAllowedTypes(['talk'])
    behavior.setImmediatelyAddableTypes(['talk'])
    logger.info('Added and configured {0}'.format(talks_folder.absolute_url()))


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
