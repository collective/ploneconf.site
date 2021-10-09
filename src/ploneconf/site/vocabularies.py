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
    # Use safe_simplevocabulary_from_values
    # as soon as safe_simplevocabulary_from_values accepts a dictionary as argument
    # return safe_simplevocabulary_from_values(values)

    normalizer = getUtility(IIDNormalizer)
    terms = [
        SimpleVocabulary.createTerm(
            normalizer.normalize(value),
            normalizer.normalize(value),
            registry_record_value[value],
        )
        for value in registry_record_value
    ]
    return SimpleVocabulary(terms)


@provider(IVocabularyFactory)
def TalkTypesVocabulary(context):
    name = "ploneconf.types_of_talk"
    registry_record_value = api.portal.get_registry_record(name)
    # Use safe_simplevocabulary_from_values
    # as soon as safe_simplevocabulary_from_values accepts a dictionary as argument
    # return safe_simplevocabulary_from_values(values)

    normalizer = getUtility(IIDNormalizer)
    terms = [
        SimpleVocabulary.createTerm(
            normalizer.normalize(value),
            normalizer.normalize(value),
            registry_record_value[value],
        )
        for value in registry_record_value
    ]
    return SimpleVocabulary(terms)


@provider(IVocabularyFactory)
def AudiencesVocabulary(context):
    name = "ploneconf.audiences"
    registry_record_value = api.portal.get_registry_record(name)
    # Use safe_simplevocabulary_from_values
    # as soon as safe_simplevocabulary_from_values accepts a dictionary as argument
    # return safe_simplevocabulary_from_values(values)

    normalizer = getUtility(IIDNormalizer)
    terms = [
        SimpleVocabulary.createTerm(
            normalizer.normalize(value),
            normalizer.normalize(value),
            registry_record_value[value],
        )
        for value in registry_record_value
    ]
    return SimpleVocabulary(terms)
