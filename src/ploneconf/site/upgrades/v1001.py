from plone import api
from plone.app.upgrade.utils import loadMigrationProfile

import logging


default_profile = "profile-ploneconf.site:default"
logger = logging.getLogger(__name__)


def reload_gs_profile(setup_tool):
    """Load default profile"""
    loadMigrationProfile(
        setup_tool,
        default_profile,
    )


def update_types(setup_tool):
    setup_tool.runImportStepFromProfile(default_profile, "typeinfo")


def cleanup_site_structure(setup_tool):
    # Load default profile including new type info
    reload_gs_profile(setup_tool)

    portal = api.portal.get()

    # Create the expected site structure
    if "training" not in portal:
        api.content.create(
            container=portal, type="Document", id="training", title="Training"
        )

    if "schedule" not in portal:
        schedule_folder = api.content.create(
            container=portal, type="Document", id="schedule", title="Schedule"
        )
    else:
        schedule_folder = portal["schedule"]
    schedule_folder_url = schedule_folder.absolute_url()

    if "location" not in portal:
        api.content.create(
            container=portal, type="Document", id="location", title="Location"
        )

    if "sponsors" not in portal:
        api.content.create(
            container=portal, type="Document", id="sponsors", title="Sponsors"
        )

    if "sprint" not in portal:
        api.content.create(
            container=portal, type="Document", id="sprint", title="Sprint"
        )

    # Find all talks
    brains = api.content.find(portal_type="talk")
    for brain in brains:
        if schedule_folder_url in brain.getURL():
            # Skip if the talk is already somewhere inside the target folder
            continue
        obj = brain.getObject()
        # Move talk to the folder '/schedule'
        api.content.move(source=obj, target=schedule_folder, safe_id=True)
        logger.info(f"{obj.absolute_url()} moved to {schedule_folder_url}")


def update_indexes(setup_tool):
    # Indexes and metadata
    setup_tool.runImportStepFromProfile(default_profile, "catalog")
    # Criterions
    setup_tool.runImportStepFromProfile(default_profile, "plone.app.registry")
    # Reindexing content
    for brain in api.content.find(portal_type=["talk", "sponsor"]):
        obj = brain.getObject()
        obj.reindexObject()
        logger.info(f"{obj.id} reindexed.")
