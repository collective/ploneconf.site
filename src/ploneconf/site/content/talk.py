# -*- coding: utf-8 -*-
from plone.app.multilingual.browser.interfaces import make_relation_root_path
from plone.app.textfield import RichText
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from ploneconf.site import _
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer


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
    directives.write_permission(audience='cmf.ReviewPortalContent')
    audience = schema.Set(
        title=_(u'Audience'),
        value_type=schema.Choice(
            vocabulary='ploneconf.audiences',
            ),
        required=False,
        )

    directives.write_permission(room='cmf.ReviewPortalContent')
    room = schema.Choice(
        title=_(u'Room'),
        vocabulary='ploneconf.rooms',
        required=False,
        )

    speaker = RelationList(
        title=u'Speaker',
        default=[],
        value_type=RelationChoice(vocabulary='plone.app.vocabularies.Catalog'),
        required=False,
        missing_value=[],
        )
    directives.widget(
        'speaker',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['speaker'],
            'basePath': make_relation_root_path,        },
        )

    speaker_fallback = schema.TextLine(
        title='Speaker Fallback',
        description='Use if there is no registered Speaker to relate to',
        required=False,
        )

    # speaker = schema.TextLine(
    #     title=_(u'Speaker'),
    #     description=_(u'Name (or names) of the speaker'),
    #     required=False,
    #     )

    # company = schema.TextLine(
    #     title=_(u'Company'),
    #     required=False,
    #     )

    # email = Email(
    #     title=_(u'Email'),
    #     description=_(u'Email adress of the speaker'),
    #     required=False,
    #     )

    # website = schema.TextLine(
    #     title=_(u'Website'),
    #     required=False,
    #     )

    # twitter = schema.TextLine(
    #     title=_(u'Twitter name'),
    #     required=False,
    #     )

    # github = schema.TextLine(
    #     title=_(u'Github username'),
    #     required=False,
    #     )

    # image = NamedBlobImage(
    #     title=_(u'Image'),
    #     description=_(u'Portrait of the speaker'),
    #     required=False,
    #     )

    # speaker_biography = RichText(
    #     title=_(u'Speaker Biography (max. 1000 characters)'),
    #     max_length=1000,
    #     required=False,
    #     )

    directives.write_permission(slides='cmf.ReviewPortalContent')
    slides = schema.TextLine(
        title=_(u'URL of the Website that holds the slides'),
        required=False,
        )

    directives.write_permission(video='cmf.ReviewPortalContent')
    video = schema.TextLine(
        title=_(u'URL of the Website that holds the video of the talk'),
        required=False,
        )

    directives.write_permission(hide_date='cmf.ReviewPortalContent')
    hide_date = schema.Bool(
        title=_(u'Hide date and time'),
        description=_(u'Display talks without date and time.'),
        required=False,
        default=True,
        )


@implementer(ITalk)
class Talk(Container):
    """Talk instance class"""
