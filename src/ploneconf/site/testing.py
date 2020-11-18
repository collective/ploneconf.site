# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ploneconf.site


class PloneconfSiteLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        import collective.folderishtypes
        import plone.app.contenttypes
        import kitconcept.volto
        import kitconcept.volto.cors
        # plone.app.contenttypes,plone.restapi,kitconcept.volto,kitconcept.volto.cors 
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.folderishtypes)
        self.loadZCML(package=plone.app.contenttypes)
        self.loadZCML(package=kitconcept.volto)
        self.loadZCML(package=kitconcept.volto.cors)
        self.loadZCML(package=ploneconf.site)

    def setUpPloneSite(self, portal):
        # plone.app.contenttypes:plone-content,plone.restapi:default,kitconcept.volto:default-homepage
        # applyProfile(portal, 'plone.restapi:default')
        applyProfile(portal, 'collective.folderishtypes.dx:default')
        # applyProfile(portal, 'plone.app.contenttypes:plone-content')
        # applyProfile(portal, 'kitconcept.volto:default')
        applyProfile(portal, 'kitconcept.volto:default-homepage')
        applyProfile(portal, 'ploneconf.site:default')


PLONECONF_SITE_FIXTURE = PloneconfSiteLayer()


PLONECONF_SITE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONECONF_SITE_FIXTURE,),
    name='PloneconfSiteLayer:IntegrationTesting',
)


PLONECONF_SITE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONECONF_SITE_FIXTURE,),
    name='PloneconfSiteLayer:FunctionalTesting',
)


PLONECONF_SITE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONECONF_SITE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PloneconfSiteLayer:AcceptanceTesting',
)
