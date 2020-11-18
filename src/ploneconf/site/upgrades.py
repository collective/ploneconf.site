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
    schedule_folder_url = schedule_folder.absolute_url()

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

    # Find all talks
    brains = api.content.find(portal_type='talk')
    for brain in brains:
        if schedule_folder_url in brain.getURL():
            # Skip if the talk is already somewhere inside the target folder
            continue
        obj = brain.getObject()
        logger.info('Moving {0} to {1}'.format(
            obj.absolute_url(), schedule_folder_url))
        # Move talk to the folder '/the-event/talks'
        api.content.move(
            source=obj,
            target=schedule_folder,
            safe_id=True)


def install_kitconcept_volto(setup):
    logger.info('install add-ons like kitconcept.volto and restore folderish behavior')
    setup.runImportStepFromProfile(default_profile, 'metadata')
    setup.runImportStepFromProfile(default_profile, 'typeinfo')
