from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IPloneconfSettings(Interface):

    talk_submission_open = schema.Bool(
        title="Allow talk submission",
        description="Allow the submission of talks for anonymous user",
        default=False,
        required=False,
    )

    types_of_talk = schema.Dict(
        title="Types of Talk",
        description="Available types of a talk",
        default={
            "talk": "Talk",
            "training": "Training",
            "keynote": "Keynote",
            "lightning-talk": "Lightning Talk",
        },
        missing_value={},
        required=False,
        key_type=schema.TextLine(),
        value_type=schema.TextLine(),
    )

    audiences = schema.Dict(
        title="Audience",
        description="Available audiences of a talk",
        default={
            "beginner": "Beginner",
            "advanced": "Advanced",
            "professional": "Professional",
        },
        missing_value={},
        required=False,
        key_type=schema.TextLine(),
        value_type=schema.TextLine(),
    )

    rooms = schema.Dict(
        title="Rooms",
        description="Available rooms of the conference",
        default={
            "101": "101",
            "201": "201",
            "auditorium": "Auditorium",
        },
        missing_value={},
        required=False,
        key_type=schema.TextLine(),
        value_type=schema.TextLine(),
    )


class PloneconfRegistryEditForm(RegistryEditForm):
    schema = IPloneconfSettings
    schema_prefix = 'ploneconf'
    label = 'Ploneconf Settings'


class PloneConfControlPanelFormWrapper(ControlPanelFormWrapper):
    form = PloneconfRegistryEditForm


@adapter(Interface, Interface)
class PloneConfRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""
    schema = IPloneconfSettings
    schema_prefix = 'ploneconf'
    configlet_id = 'ploneconf-controlpanel'
    configlet_category_id = 'Products'
    title = 'Ploneconf Settings'
    group = 'Products'
