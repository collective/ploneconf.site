from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import implementer


class ISponsor(model.Schema):
    """Dexterity schema for sponsors"""

    level = schema.Choice(
        title="Sponsoring Level", values=["bronze", "silver", "gold"], required=True
    )

    text = RichText(title="Text", required=False)

    url = schema.URI(title="Link", required=False)

    fieldset("Images", fields=["image", "advertisement"])
    image = namedfile.NamedBlobImage(
        title="Logo",
        required=False,
    )

    advertisement = namedfile.NamedBlobImage(
        title="Advertisement (Gold-sponsors and above)",
        required=False,
    )

    directives.read_permission(notes="plone.app.controlpanel.Site")
    directives.write_permission(notes="plone.app.controlpanel.Site")
    notes = RichText(
        title="Secret Notes (only for site-administrators and managers)", required=False
    )


@implementer(ISponsor)
class Sponsor(Container):
    """Sponsor instance class"""
