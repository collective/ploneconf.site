from plone import api
from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import getUtility
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@provider(IVocabularyFactory)
def RoomsVocabularyFactory(context):
    name = "ploneconf.rooms"
    registry_record_value = api.portal.get_registry_record(name)
    return SimpleVocabulary.fromItems([[el[0], el[0], el[1]] for el in registry_record_value.items()])


@provider(IVocabularyFactory)
def TalkTypesVocabulary(context):
    name = "ploneconf.types_of_talk"
    registry_record_value = api.portal.get_registry_record(name)
    return SimpleVocabulary.fromItems([[el[0], el[0], el[1]] for el in registry_record_value.items()])


@provider(IVocabularyFactory)
def AudiencesVocabulary(context):
    name = "ploneconf.audiences"
    registry_record_value = api.portal.get_registry_record(name)
    return SimpleVocabulary.fromItems([[el[0], el[0], el[1]] for el in registry_record_value.items()])
