import time
from datetime import datetime
from utils import compute_time
import logging
import Globals
import os.path
from AccessControl import getSecurityManager,ClassSecurityInfo
from Products.Five import BrowserView

from zope.component import getUtility

from Acquisition import aq_parent
from DateTime import DateTime

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Acquisition import aq_inner

from collective.portlet.recentactivity.interfaces import IRecentActivityUtility

from zope.component import getUtility
from collective.portlet.recentactivity.interfaces import IRecentActivityUtility


class RecentActivityView(BrowserView):

    template = ViewPageTemplateFile('recentactivity.pt')

    def __call__(self):
        """View the recent activity on a separate page.
        """
        self.request.set('disable_border', True)
        return self.template()

    def recent_activities(self):
        context = aq_inner(self.context)
        activities = getUtility(IRecentActivityUtility)
        for brain in activities.getRecentActivity(100):
             activity = brain[1]
             yield dict(time=compute_time(int(time.time()) - brain[0]),
                        action=activity['action'],
                        user=activity['user'],
                        user_url="%s/author/%s" % (context.portal_url(), activity['user']),
                        object=activity['object'],
                        object_url=activity['object_url'],
                        parent=activity['parent'],
                        parent_url=activity['parent_url'],
                        )