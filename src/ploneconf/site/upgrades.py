# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from plone import api
from plone.app.upgrade.utils import loadMigrationProfile

import logging

default_profile = 'profile-ploneconf.site:default'
logger = logging.getLogger(__name__)


def reload_gs_profile(context):
    loadMigrationProfile(
        context,
        'profile-ploneconf.site:default',
    )


def upgrade_site(setup):
    setup.runImportStepFromProfile(default_profile, 'typeinfo')
    portal = api.portal.get()
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
    talks_url = talks_folder.absolute_url()

    # Find all talks
    brains = api.content.find(portal_type='talk')
    for brain in brains:
        if talks_url in brain.getURL():
            # Skip if the talk is already somewhere inside the target folder
            continue
        obj = brain.getObject()
        logger.info('Moving {} to {}'.format(
            obj.absolute_url(), talks_folder.absolute_url()))
        # Move talk to the folder '/the-event/talks'
        api.content.move(
            source=obj,
            target=talks_folder,
            safe_id=True)
