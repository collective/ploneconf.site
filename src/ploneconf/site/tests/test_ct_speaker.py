# -*- coding: utf-8 -*-
from ploneconf.site.content.speaker import ISpeaker  # NOQA E501
from ploneconf.site.testing import PLONECONF_SITE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class SpeakerIntegrationTest(unittest.TestCase):

    layer = PLONECONF_SITE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_speaker_schema(self):
        fti = queryUtility(IDexterityFTI, name='speaker')
        schema = fti.lookupSchema()
        self.assertEqual(ISpeaker, schema)

    def test_ct_speaker_fti(self):
        fti = queryUtility(IDexterityFTI, name='speaker')
        self.assertTrue(fti)

    def test_ct_speaker_factory(self):
        fti = queryUtility(IDexterityFTI, name='speaker')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ISpeaker.providedBy(obj),
            u'ISpeaker not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_speaker_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='speaker',
            id='speaker',
        )

        self.assertTrue(
            ISpeaker.providedBy(obj),
            u'ISpeaker not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('speaker', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('speaker', parent.objectIds())

    def test_ct_speaker_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='speaker')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_speaker_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='speaker')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'speaker_id',
            title='speaker container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
