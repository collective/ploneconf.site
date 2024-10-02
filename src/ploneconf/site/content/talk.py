from plone.app.dexterity import textindexer
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer


class ITalk(model.Schema):
    """Dexterity-Schema for Talks"""

    type_of_talk = schema.Choice(
        title="Type of talk",
        vocabulary="ploneconf.types_of_talk",
        required=True,
    )

    textindexer.searchable("details")
    details = RichText(
        title="Details",
        description="Description of the talk (max. 2000 characters)",
        max_length=2000,
        required=True,
    )

    audience = schema.Set(
        title="Audience",
        value_type=schema.Choice(
            vocabulary="ploneconf.audiences",
        ),
        required=False,
    )

    speaker = RelationList(
        title="Speaker",
        description="Speakers of the talk",
        value_type=RelationChoice(vocabulary="ploneconf.speakers"),
        required=False,
        default=[],
    )

    image = NamedBlobImage(
        title="Image",
        description="Portrait of the speaker",
        required=False,
    )

    room = schema.Choice(
        title="Room",
        vocabulary="ploneconf.rooms",
        required=False,
    )


@implementer(ITalk)
class Talk(Container):
    """Talk instance class"""
