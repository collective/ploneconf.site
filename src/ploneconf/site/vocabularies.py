# -*- coding: utf-8 -*-
from plone import api
from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory


@provider(IVocabularyFactory)
def RoomsVocabularyFactory(context):
    name = 'ploneconf.rooms'
    values = api.portal.get_registry_record(name)
    return safe_simplevocabulary_from_values(values)


@provider(IVocabularyFactory)
def TalkTypesVocabulary(context):
    name = 'ploneconf.types_of_talk'
    values = api.portal.get_registry_record(name)
    return safe_simplevocabulary_from_values(values)


@provider(IVocabularyFactory)
def AudiencesVocabulary(context):
    name = 'ploneconf.audiences'
    values = api.portal.get_registry_record(name)
    return safe_simplevocabulary_from_values(values)
