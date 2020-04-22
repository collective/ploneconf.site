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
    # Create the expected folder-structure
    if 'training' not in portal:
        training_folder = api.content.create(
            container=portal,
            type='Document',
            id='training',
            title=u'Training')
    else:
        training_folder = portal['training']

    if 'schedule' not in portal:
        schedule_folder = api.content.create(
            container=portal,
            type='Document',
            id='schedule',
            title=u'Schedule')
    else:
        schedule_folder = portal['schedule']

    if 'location' not in portal:
        location_folder = api.content.create(
            container=portal,
            type='Document',
            id='location',
            title=u'Location')
    else:
        location_folder = portal['location']

    if 'sponsors' not in portal:
        sponsors_folder = api.content.create(
            container=portal,
            type='Document',
            id='sponsors',
            title=u'Sponsors')
    else:
        sponsors_folder = portal['sponsors']

    if 'sprint' not in portal:
        sprint_folder = api.content.create(
            container=portal,
            type='Document',
            id='sprint',
            title=u'Sprint')
    else:
        sprint_folder = portal['sprint']

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
