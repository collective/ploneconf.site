# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from ploneconf.site import _
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


LevelVocabulary = SimpleVocabulary(
    [SimpleTerm(value=u'platinum', title=_(u'Platinum Sponsor')),
     SimpleTerm(value=u'gold', title=_(u'Gold Sponsor')),
     SimpleTerm(value=u'silver', title=_(u'Silver Sponsor')),
     SimpleTerm(value=u'bronze', title=_(u'Bronze Sponsor'))]
    )


class ISponsor(model.Schema):
    """Dexterity Schema for Sponsors
    """

    directives.widget(level=RadioFieldWidget)
    level = schema.Choice(
        title=_(u'Sponsoring Level'),
        vocabulary=LevelVocabulary,
        required=True
    )

    text = RichText(
        title=_(u'Text'),
        required=False
    )

    url = schema.URI(
        title=_(u'Link'),
        required=False
    )

    fieldset('Images', fields=['logo', 'advertisment'])
    logo = namedfile.NamedBlobImage(
        title=_(u'Logo'),
        required=False,
    )

    advertisment = namedfile.NamedBlobImage(
        title=_(u'Advertisement (Gold-sponsors and above)'),
        required=False,
    )

    directives.read_permission(notes='cmf.ManagePortal')
    directives.write_permission(notes='cmf.ManagePortal')
    notes = RichText(
        title=_(u'Secret Notes (only for site-admins)'),
        required=False
    )
