from AccessControl import getSecurityManager
from zope.component import getUtility
from Acquisition import aq_parent
from DateTime import DateTime
from collective.portlet.recentactivity.interfaces import IRecentActivityUtility


def Added(event):
    activities = getUtility(IRecentActivityUtility)
    username = getSecurityManager().getUser().getId()
    fullname = getSecurityManager().getUser().getProperty('fullname')
    activities.addActivity(DateTime(),
                           "added",
                            username,
                            fullname,
                            event.object,
                            aq_parent(event.object))


def Edited(event):
    activities = getUtility(IRecentActivityUtility)
    username = getSecurityManager().getUser().getId()
    fullname = getSecurityManager().getUser().getProperty('fullname')
    activities.addActivity(DateTime(),
                           "edited",
                            username,
                            fullname,
                            event.object,
                            aq_parent(event.object))


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
