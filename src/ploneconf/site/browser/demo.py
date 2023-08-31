from Products.Five import BrowserView
from plone import api
from plone.app.textfield.value import RichTextValue
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides

try:
    from training.votable.behaviors.votable import IVotable

    VOTABLE_INSTALLED = True
except ImportError:
    VOTABLE_INSTALLED = False


import json
import logging
import requests

logger = logging.getLogger(__name__)


class DebugView(BrowserView):
    def __call__(self):
        """Call with /@@debugview."""
        if VOTABLE_INSTALLED:
            voting = IVotable(self.context)
            print(voting)
            print(voting.votes)
            print(voting.average_vote())
            return voting.votes


class DemoContent(BrowserView):
    def __call__(self):
        """Call with /@@create_demo_talks."""
        self.create_talks()
        return self.request.response.redirect(self.context.absolute_url())

    def create_talks(self, amount=5):
        """Create some talks"""

        alsoProvides(self.request, IDisableCSRFProtection)
        wiki_content = self.get_wikipedia_content_of_the_day()
        for data in wiki_content[:amount]:
            title = data["titles"]["normalized"]
            details = RichTextValue(
                raw=data["extract_html"],
                mimeType="text/html",
                outputMimeType="text/html",
                encoding="utf-8",
            )
            talk = api.content.create(
                container=self.context,
                type="talk",
                title=title[:20] + "..." if len(title) > 20 else title,
                description=data["description"],
                details=details,
                type_of_talk="talk",
            )
            api.content.transition(talk, to_state="published")
            logger.info(f"Created talk {talk.absolute_url()}")
        api.portal.show_message(f"Created {amount} talks!", self.request)

    def get_wikipedia_content_of_the_day(self):
        wiki = requests.get(
            "https://en.wikipedia.org/api/rest_v1/feed/featured/2023/01/02"
        )
        return json.loads(wiki.text)["mostread"]["articles"]
