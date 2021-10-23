from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider

@provider(IFormFieldProvider)
class IFeatured(model.Schema):

    featured = schema.Bool(
        title='Show this item on the frontpage',
        required=False,
    )
