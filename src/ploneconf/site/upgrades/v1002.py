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


def update_talks(setup_tool):
    # Load default profile including new type info.
    reload_gs_profile(setup_tool)

    # Find all talks
    brains = api.content.find(portal_type="talk")
    for brain in brains:
        obj = brain.getObject()
        # Update talk field 'speaker' to relation field
        if (type(obj.speaker)) == str:
            obj.speaker = []
            logger.info(f"{obj.absolute_url()} updated.")
