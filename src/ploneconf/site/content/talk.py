from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class ITalk(model.Schema):
    """Dexterity-Schema for Talks"""

    directives.widget(type_of_talk=RadioFieldWidget)
    type_of_talk = schema.Choice(
        title='Type of talk',
        values=['Talk', 'Training', 'Keynote'],
        required=True,
    )

    details = RichText(
        title='Details',
        description='Description of the talk (max. 2000 characters)',
        max_length=2000,
        required=True,
    )

    directives.widget(audience=CheckBoxFieldWidget)
    audience = schema.Set(
        title='Audience',
        value_type=schema.Choice(
            values=['Beginner', 'Advanced', 'Professional'],
        ),
        required=False,
    )

    speaker = schema.TextLine(
        title='Speaker',
        description='Name (or names) of the speaker',
        required=False,
    )

    company = schema.TextLine(
        title='Company',
        required=False,
    )

    email = Email(
        title='Email',
        description='Email adress of the speaker',
        required=False,
    )

    website = schema.TextLine(
        title='Website',
        required=False,
    )

    twitter = schema.TextLine(
        title='Twitter name',
        required=False,
    )

    github = schema.TextLine(
        title='Github username',
        required=False,
    )

    image = NamedBlobImage(
        title='Image',
        description='Portrait of the speaker',
        required=False,
    )

    speaker_biography = RichText(
        title='Speaker Biography (max. 1000 characters)',
        max_length=1000,
        required=False,
    )


@implementer(ITalk)
class Talk(Container):
    """Talk instance class"""
