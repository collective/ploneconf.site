# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView

import datetime


class FrontpageView(BrowserView):
    """The view of the conference frontpage
    """

    def talks(self):
        """Get today's talks"""
        results = []
        today = datetime.date.today()
        brains = api.content.find(
            portal_type='talk',
            sort_on='start',
            sort_order='descending',
        )
        for brain in brains:
            if brain.start.date() == today:
                results.append({
                    'title': brain.Title,
                    'description': brain.Description,
                    'url': brain.getURL(),
                    'audience': ', '.join(brain.audience or []),
                    'type_of_talk': brain.type_of_talk,
                    'speaker': brain.speaker,
                    'room': brain.room,
                    'start': brain.start,
                    })
        return results
