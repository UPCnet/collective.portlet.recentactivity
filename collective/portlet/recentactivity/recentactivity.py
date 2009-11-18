from datetime import datetime
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

logger = logging.getLogger('RecentActivity')
logger.setLevel(logging.INFO)


def Added(event):
    activities = getUtility(IRecentActivityUtility)
    activities.addActivity(DateTime(),
                           "added",
                            getSecurityManager().getUser().getId(),
                            event.object, 
                            aq_parent(event.object))
    logger.log(logging.INFO, 
               "User %s %s %s to %s." % \
               (getSecurityManager().getUser().getId(),
                "added",
                event.object,
                aq_parent(event.object)))

def Edited(event):
    activities = getUtility(IRecentActivityUtility)
    activities.addActivity(DateTime(),
                           "edited",
                            getSecurityManager().getUser().getId(),
                            event.object, 
                            aq_parent(event.object))    
    logger.log(logging.INFO, 
               "User %s %s %s to %s" % \
               (getSecurityManager().getUser().getId(),
                "modified",
                event.object,
                aq_parent(event.object)))
    
def Copied(event):
    """
    """
    pass
    #activities = getUtility(IRecentActivityUtility)
    #activities.addActivity(DateTime(),
    #                       "copied",
    #                       getSecurityManager().getUser().getId(),                           
    #                       event.object,
    #                       aq_parent(event.object))
    #logger.log(logging.INFO,"addActivity(%s, %s, %s, %s, %s)", DateTime(), "modified", getSecurityManager().getUser().getId(), event.object, aq_parent(event.object)) 

def Moved(event):
    """
    """
    pass
    #if event.oldParent==None:
	#op=""
    #else:
	#op=event.oldParent
    #if event.newParent==None:
	#np=""
    #else:
	#np=event.newParent
    #name = getSecurityManager().getUser().getId()
    #logger.log(logging.INFO,"moved %s from %s to %s by %s", event.object, op, np, name)

def Removed(event):
    """
    """
    pass

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
        u = getUtility(IRecentActivityUtility)
        return u.getRecentActivity(5)
