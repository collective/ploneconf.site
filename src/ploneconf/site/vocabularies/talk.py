from plone import api
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@provider(IVocabularyFactory)
def TalkTypesVocabulary(context):
    name = "ploneconf.types_of_talk"
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    lang = lang.split("-")[0]
    return SimpleVocabulary.fromItems(
        [
            [item["token"], item["token"], item["titles"].get(lang, item["token"])]
            for item in items
        ]
    )


@provider(IVocabularyFactory)
def AudiencesVocabulary(context):
    name = "ploneconf.audiences"
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    lang = lang.split("-")[0]
    return SimpleVocabulary.fromItems(
        [
            [item["token"], item["token"], item["titles"].get(lang, item["token"])]
            for item in items
        ]
    )


@provider(IVocabularyFactory)
def RoomsVocabularyFactory(context):
    name = "ploneconf.rooms"
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    lang = lang.split("-")[0]
    return SimpleVocabulary.fromItems(
        [
            [item["token"], item["token"], item["titles"].get(lang, item["token"])]
            for item in items
        ]
    )
