# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import directives
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IFeatured(model.Schema):

    directives.fieldset(
        'featured',
        label=u'Featured',
        fields=('featured',),
    )

    featured = schema.Bool(
        title=u'Show this item on the frontpage',
        required=False,
    )
