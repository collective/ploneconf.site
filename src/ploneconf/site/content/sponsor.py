from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import implementer


class ISponsor(model.Schema):
    """Dexterity Schema for Sponsors"""

    level = schema.Choice(
        title="Sponsoring Level", vocabulary="ploneconf.sponsor_levels", required=True
    )

    text = RichText(title="Text", required=False)

    url = schema.URI(title="Link", required=False)

    fieldset("Images", fields=["logo", "advertisement"])
    logo = namedfile.NamedBlobImage(
        title="Logo",
        required=False,
    )

    advertisement = namedfile.NamedBlobImage(
        title="Advertisement (Gold-sponsors and above)",
        required=False,
    )

    directives.read_permission(notes="cmf.ManagePortal")
    directives.write_permission(notes="cmf.ManagePortal")
    notes = RichText(title="Secret Notes (only for site-admins)", required=False)


@implementer(ISponsor)
class Sponsor(Container):
    """Sponsor instance class"""
