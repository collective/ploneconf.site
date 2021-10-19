from plone import api
from plone.app.upgrade.utils import loadMigrationProfile

import logging

default_profile = "profile-ploneconf.site:default"
logger = logging.getLogger(__name__)


def reload_gs_profile(context):
    loadMigrationProfile(
        context,
        "profile-ploneconf.site:default",
    )


def upgrade_site(context=None):
    # reload type info
    setup = api.portal.get_tool("portal_setup")
    setup.runImportStepFromProfile(default_profile, "typeinfo")
    portal = api.portal.get()

    # Create the expected folder-structure
    if "schedule" not in portal:
        schedule_folder = api.content.create(
            container=portal, type="Document", id="schedule", title=u"Schedule"
        )
    else:
        schedule_folder = portal["schedule"]
    schedule_folder_url = schedule_folder.absolute_url()

    if "sponsors" not in portal:
        api.content.create(
            container=portal, type="Document", id="sponsors", title=u"Sponsors"
        )

    # Find all talks and move to schedule
    brains = api.content.find(portal_type="talk")
    for brain in brains:
        if schedule_folder_url in brain.getURL():
            # Skip if the talk is already somewhere inside the target folder
            continue
        obj = brain.getObject()
        logger.info("Moving {} to {}".format(obj.absolute_url(), schedule_folder_url))
        # Move talk to the folder '/schedule'
        api.content.move(source=obj, target=schedule_folder, safe_id=True)
