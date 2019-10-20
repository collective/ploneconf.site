# -*- coding: utf-8 -*-
from datetime import date
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from ploneconf.site import _
from zope import schema
from zope.interface import Interface


class IPloneconfControlPanel(Interface):

    date_of_conference = schema.Date(
        title=_(u'First day of the conference'),
        required=False,
        default=date(2019, 10, 17),
    )

    talk_submission_open = schema.Bool(
        title=_(u'Allow talk submission'),
        description=_(u'Allow the submission of talks for anonymous user'),
        default=False,
        required=False,
    )

    type_of_talk = schema.List(
        title=_(u'Available types for talks'),
        default=[u'Talk', u'Training', u'Keynote', u'Lightning Talk'],
        missing_value=None,
        required=False,
        value_type=schema.TextLine(),
    )

    room = schema.List(
        title=_(u'Available Rooms for the conference'),
        default=[u'101', u'201', u'Auditorium'],
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )

    audience = schema.List(
        title=_(u'Available audiences for talks'),
        default=[u'Beginner', u'Advanced', u'Professionals'],
        missing_value=None,
        required=False,
        value_type=schema.TextLine()
    )


class PloneconfControlPanelForm(RegistryEditForm):
    schema = IPloneconfControlPanel
    schema_prefix = "ploneconf"
    label = _(u'Ploneconf Settings')


PloneconfControlPanelView = layout.wrap_form(
    PloneconfControlPanelForm, ControlPanelFormWrapper)
