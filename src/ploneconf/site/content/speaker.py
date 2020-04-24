# -*- coding: utf-8 -*-
from dexterity.membrane.behavior.user import DxUserObject
from dexterity.membrane.content.member import IMember
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
# from plone.namedfile import field as namedfile
# from plone.supermodel import model
# from plone.supermodel.directives import fieldset
from ploneconf.site import _
from Products.membrane.interfaces import IMembraneUserRoles
# from z3c.form.browser.radio import RadioFieldWidget
from zope.component import adapter
# from zope import schema
from zope.interface import implementer


class ISpeaker(IMember):
    """ Marker interface and Dexterity Python Schema for Speaker
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('speaker.xml')

    speaker_biography = RichText(
        title=_(u'Speaker Biography (max. 1000 characters)'),
        max_length=1000,
        required=False,
        )

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(ISpeaker)
class Speaker(Container):
    """
    """


DEFAULT_ROLES = ['Ploneconf Member', 'Member']


@implementer(IMembraneUserRoles)
@adapter(ISpeaker)
class MyDefaultRoles(DxUserObject):

    def getRolesForPrincipal(self, principal, request=None):
        return DEFAULT_ROLES
