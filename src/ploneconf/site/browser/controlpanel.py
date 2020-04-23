# -*- coding: utf-8 -*-
from datetime import date
from ploneconf.site import _
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface


class IPloneconfControlPanel(Interface):

    date_of_conference = schema.Date(
        title=u'First day of the conference',
        required=False,
        default=date(2050, 9, 13),
    )

    talk_submission_open = schema.Bool(
        title=u'Allow talk submission',
        description=u'Allow the submission of talks for anonymous user',
        default=False,
        required=False,
    )

    rooms = schema.List(
        title=u'Available Rooms for the conference',
        default=[u'101', u'201', u'Auditorium'],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    types_of_talk = schema.List(
        title=u'Available types for talks',
        default=[u'Talk', u'Training', u'Keynote', u'Lightning Talk'],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    audiences = schema.List(
        title=u'Available audiences for talks',
        default=[u'Beginner', u'Advanced', u'Professional'],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )


class PloneconfControlPanelForm(RegistryEditForm):
    schema = IPloneconfControlPanel
    schema_prefix = 'ploneconf'
    label = u'Ploneconf Settings'


PloneconfControlPanelView = layout.wrap_form(
    PloneconfControlPanelForm, ControlPanelFormWrapper)
