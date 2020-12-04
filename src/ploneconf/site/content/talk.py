# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from ploneconf.site import _
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class ITalk(model.Schema):
    """Dexterity-Schema for Talks"""

    directives.widget(type_of_talk=RadioFieldWidget)
    type_of_talk = schema.Choice(
        title=_(u'Type of talk'),
        vocabulary='ploneconf.types_of_talk',
        required=True,
        )

    details = RichText(
        title=_(u'Details'),
        description=_(u'Description of the talk (max. 2000 characters)'),
        max_length=2000,
        required=True,
        )

    directives.widget(audience=CheckBoxFieldWidget)
    audience = schema.Set(
        title=_(u'Audience'),
        value_type=schema.Choice(vocabulary='ploneconf.audiences'),
        required=False,
        )

    speaker = schema.TextLine(
        title=_(u'Speaker'),
        description=_(u'Name (or names) of the speaker'),
        required=False,
        )

    company = schema.TextLine(
        title=_(u'Company'),
        required=False,
        )

    email = Email(
        title=_(u'Email'),
        description=_(u'Email adress of the speaker'),
        required=False,
        )

    website = schema.TextLine(
        title=_(u'Website'),
        required=False,
        )

    twitter = schema.TextLine(
        title=_(u'Twitter name'),
        required=False,
        )

    github = schema.TextLine(
        title=_(u'Github username'),
        required=False,
        )

    image = NamedBlobImage(
        title=_(u'Image'),
        description=_(u'Portrait of the speaker'),
        required=False,
        )

    speaker_biography = RichText(
        title=_(u'Speaker Biography (max. 1000 characters)'),
        max_length=1000,
        required=False,
        )

    room = schema.Choice(
        title=_(u'Room'),
        vocabulary='ploneconf.rooms',
        required=False,
        )


@implementer(ITalk)
class Talk(Container):
    """Talk instance class"""
