# -*- coding: utf-8 -*-
from dexterity.membrane.behavior.user import DxUserObject
from dexterity.membrane.content.member import IEmail
from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.schema.email import Email
# from plone.supermodel import model
# from plone.supermodel.directives import fieldset
from ploneconf.site import _
from Products.membrane.interfaces import IMembraneUserRoles
# from z3c.form.browser.radio import RadioFieldWidget
from zope.component import adapter
from zope import schema
from zope.interface import implementer


class ISpeaker(IEmail):
    """ Marker interface and Dexterity Python Schema for Speaker
    """

    first_name = schema.TextLine(
        title=_(u'First Name'),
        required=True,
    )

    last_name = schema.TextLine(
        title=_(u'Last Name'),
        required=True,
    )

    company = schema.TextLine(
        title=_(u'Company'),
        required=False,
        )

    job_title = schema.TextLine(
        title=_(u'Job Title'),
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

    image = namedfile.NamedBlobImage(
        title=_(u'Image'),
        description=_(u'Portrait of the speaker'),
        required=False,
        )

    speaker_biography = RichText(
        title=_(u'Speaker Biography (max. 1000 characters)'),
        max_length=1000,
        required=False,
        )


@implementer(ISpeaker)
class Speaker(Item):
    """
    """


DEFAULT_ROLES = ['Ploneconf Member', 'Member']


@implementer(IMembraneUserRoles)
@adapter(ISpeaker)
class MyDefaultRoles(DxUserObject):

    def getRolesForPrincipal(self, principal, request=None):
        return DEFAULT_ROLES
