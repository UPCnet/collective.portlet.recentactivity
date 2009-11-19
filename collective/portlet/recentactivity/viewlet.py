from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from zope.component import getUtility
from collective.portlet.recentactivity.interfaces import IRecentActivityUtility

from Acquisition import aq_inner
from plone.memoize.instance import memoize

import time

class RecentActivityViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlet.pt')

    def recent_activities(self):
        context = aq_inner(self.context)        
        for brain in self._data():
            activity = brain[1]
            time_since_activity = (int(time.time()) - brain[0])/60
            yield dict(time=time_since_activity,
                       action=activity['action'],
                       user=activity['user'],
                       user_url="%s/%s" % (context.portal_url(), activity['user']),
                       object=activity['object'],
                       object_url=activity['object_url'],
                       parent=activity['parent'],
                       parent_url=activity['parent_url'],
                       )
                                        
    def recently_modified_link(self):
        return '%s/@@recent-activity' % self.portal_url
    
    @memoize
    def _data(self):
        # XXX: do we want the limit to be configurable?
        limit = 5
        activities = getUtility(IRecentActivityUtility)
        return activities.getRecentActivity(limit)