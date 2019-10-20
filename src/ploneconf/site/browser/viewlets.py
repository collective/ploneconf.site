# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import ViewletBase
from ploneconf.site.behaviors.featured import IFeatured


class FeaturedViewlet(ViewletBase):

    def is_featured(self):
        adapted = IFeatured(self.context)
        return adapted.featured
