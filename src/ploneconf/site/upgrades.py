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
    # reload type info
    setup.runImportStepFromProfile(default_profile, 'typeinfo')
    portal = api.portal.get()

    # Create the expected folder-structure
    if 'training' not in portal:
        training_folder = api.content.create(
            container=portal,
            type='Folder',
            id='training',
            title=u'Training')
    else:
        training_folder = portal['training']

    if 'schedule' not in portal:
        schedule_folder = api.content.create(
            container=portal,
            type='Folder',
            id='schedule',
            title=u'Schedule')
    else:
        schedule_folder = portal['schedule']
    schedule_folder_url = schedule_folder.absolute_url()

    if 'location' not in portal:
        location_folder = api.content.create(
            container=portal,
            type='Folder',
            id='location',
            title=u'Location')
    else:
        location_folder = portal['location']

    if 'sponsors' not in portal:
        sponsors_folder = api.content.create(
            container=portal,
            type='Folder',
            id='sponsors',
            title=u'Sponsors')
    else:
        sponsors_folder = portal['sponsors']

    if 'sprint' not in portal:
        sprint_folder = api.content.create(
            container=portal,
            type='Folder',
            id='sprint',
            title=u'Sprint')
    else:
        sprint_folder = portal['sprint']

    # Find all talks
    brains = api.content.find(portal_type='talk')
    for brain in brains:
        if schedule_folder_url in brain.getURL():
            # Skip if the talk is already somewhere inside the target folder
            continue
        obj = brain.getObject()
        logger.info('Moving {} to {}'.format(
            obj.absolute_url(), schedule_folder_url))
        # Move talk to the folder '/the-event/talks'
        api.content.move(
            source=obj,
            target=schedule_folder,
            safe_id=True)
