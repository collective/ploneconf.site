from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IPloneconfControlPanel(Interface):

    talk_submission_open = schema.Bool(
        title="Allow talk submission",
        description="Allow the submission of talks for anonymous user",
        default=False,
        required=False,
    )

    types_of_talk = schema.List(
        title="Available types for talks",
        default=["Talk", "Training", "Keynote", "Lightning Talk"],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    audiences = schema.List(
        title="Available audiences for talks",
        default=["Beginner", "Advanced", "Professional"],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    rooms = schema.Tuple(
        title="Available Rooms for the conference",
        default=("101", "201", "Auditorium"),
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )


@adapter(Interface, Interface)
class PloneconfControlPanel(RegistryConfigletPanel):
    schema = IPloneconfControlPanel
    schema_prefix = "ploneconf"
    configlet_id = "ploneconf-controlpanel"
    configlet_category_id = "General"
    title = "Ploneconf Settings"
    group = "Products"


class PloneconfControlPanelForm(RegistryEditForm):
    schema = IPloneconfControlPanel
    schema_prefix = "ploneconf"
    label = "Ploneconf Settings"


PloneconfControlPanelView = layout.wrap_form(
    PloneconfControlPanelForm, ControlPanelFormWrapper
)
