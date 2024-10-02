from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory


@provider(IVocabularyFactory)
def SpeakerVocabularyFactory(context=None):
    return StaticCatalogVocabulary(
        {
            "portal_type": ["speaker"],
            # "review_state": "published",
            "sort_on": "sortable_title",
        }
    )
