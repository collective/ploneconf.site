# -*- coding: utf-8 -*-
from collections import OrderedDict
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize import ram
from ploneconf.site.behaviors.featured import IFeatured
from ploneconf.site.content.sponsor import LevelVocabulary
from random import shuffle
from time import time


class FeaturedViewlet(ViewletBase):

    def is_featured(self):
        adapted = IFeatured(self.context)
        return adapted.featured


class SponsorsViewlet(ViewletBase):

    @ram.cache(lambda *args: time() // (60 * 60))
    def _sponsors(self):
        results = []
        for brain in api.content.find(portal_type='sponsor'):
            obj = brain.getObject()
            scales = api.content.get_view(
                name='images',
                context=obj,
                request=self.request)
            scale = scales.scale(
                'logo',
                width=200,
                height=80,
                direction='down')
            tag = scale.tag() if scale else None
            if not tag:
                # only display sponsors with a logo
                continue
            results.append({
                'title': obj.title,
                'description': obj.description,
                'tag': tag,
                'url': obj.url or obj.absolute_url(),
                'level': obj.level
            })
        return results

    def sponsors(self):
        sponsors = self._sponsors()
        if not sponsors:
            return
        results = OrderedDict()
        levels = [i.value for i in LevelVocabulary]
        for level in levels:
            level_sponsors = []
            for sponsor in sponsors:
                if level == sponsor['level']:
                    level_sponsors.append(sponsor)
            if not level_sponsors:
                continue
            shuffle(level_sponsors)
            results[level] = level_sponsors
        return results
