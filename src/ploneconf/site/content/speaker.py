from plone.app.dexterity import textindexer
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class ISpeaker(model.Schema):
    """Dexterity-Schema for Speakers"""

    textindexer.searchable("company")
    company = schema.TextLine(
        title="Company",
        required=False,
    )

    email = Email(
        title="Email",
        description="Email address of the speaker",
        required=False,
    )

    website = schema.TextLine(
        title="Website",
        required=False,
    )

    github = schema.TextLine(
        title="Github username",
        required=False,
    )

    image = NamedBlobImage(
        title="Image",
        description="Portrait of the speaker",
        required=False,
    )

    textindexer.searchable("speaker_biography")
    speaker_biography = RichText(
        title="Speaker Biography (max. 1000 characters)",
        max_length=1000,
        required=False,
    )


@implementer(ISpeaker)
class Speaker(Container):
    """Speaker instance class"""
