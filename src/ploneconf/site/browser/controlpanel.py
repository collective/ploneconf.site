from plone import schema
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.autoform import directives
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import Interface

import json

VOCABULARY_SCHEMA = json.dumps(
    {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "token": {"type": "string"},
                        "titles": {
                            "type": "object",
                            "properties": {
                                "lang": {"type": "string"},
                                "title": {"type": "string"},
                            },
                        },
                    },
                },
            }
        },
    }
)


class IPloneconfSettings(Interface):

    talk_submission_open = schema.Bool(
        title="Allow talk submission",
        description="Allow the submission of talks for anonymous user",
        default=False,
        required=False,
    )

    types_of_talk = schema.JSONField(
        title="Types of Talk",
        description="Available types of a talk",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={
            "items": [
                {
                    "token": "talk",
                    "titles": {
                        "en": "Talk",
                        "de": "Vortrag",
                    },
                },
                {
                    "token": "lightning-talk",
                    "titles": {
                        "en": "Lightning-Talk",
                        "de": "Lightning-Talk",
                    },
                },
                {
                    "token": "keynote",
                    "titles": {
                        "en": "Keynote",
                        "de": "Keynote",
                    },
                },
            ]
        },
        missing_value={"items": []},
    )
    directives.widget(
        "types_of_talk",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

    audiences = schema.JSONField(
        title="Audience",
        description="Available audiences of a talk",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={
            "items": [
                {
                    "token": "beginner",
                    "titles": {
                        "en": "Beginner",
                        "de": "Anfänger",
                    },
                },
                {
                    "token": "advanced",
                    "titles": {
                        "en": "Advanced",
                        "de": "Fortgeschrittene",
                    },
                },
                {
                    "token": "professional",
                    "titles": {
                        "en": "Professional",
                        "de": "Profi",
                    },
                },
            ]
        },
        missing_value={"items": []},
    )
    directives.widget(
        "audiences",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

    rooms = schema.JSONField(
        title="Rooms",
        description="Available rooms of the conference",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={
            "items": [
                {
                    "token": "101",
                    "titles": {
                        "en": "101",
                        "de": "101",
                    },
                },
                {
                    "token": "201",
                    "titles": {
                        "en": "201",
                        "de": "201",
                    },
                },
                {
                    "token": "auditorium",
                    "titles": {
                        "en": "Auditorium",
                        "de": "Auditorium",
                    },
                },
            ]
        },
        missing_value={"items": []},
    )
    directives.widget(
        "rooms",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )


class PloneconfRegistryEditForm(RegistryEditForm):
    schema = IPloneconfSettings
    schema_prefix = "ploneconf"
    label = "Ploneconf Settings"



class PloneConfControlPanelFormWrapper(ControlPanelFormWrapper):
    form = PloneconfRegistryEditForm


@adapter(Interface, Interface)
class PloneConfRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IPloneconfSettings
    schema_prefix = "ploneconf"
    configlet_id = "ploneconf-controlpanel"
    configlet_category_id = "Products"
    title = "Ploneconf Settings"
    group = "Products"
