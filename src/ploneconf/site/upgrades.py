from plone import api
import logging

logger = logging.getLogger("ploneconf.site")

PROFILE_ID = "profile-ploneconf.site:default"


def updateRegistry(context):
    setup = api.portal.get_tool("portal_setup")
    setup.runImportStepFromProfile(PROFILE_ID, "plone.app.registry")
    logger.info("Registry updated")
