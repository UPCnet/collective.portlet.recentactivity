# -*- encoding: utf-8 -*-

import time

from zope.interface import implements
from zope.app.container.btree import BTreeContainer

from OFS.SimpleItem import SimpleItem
from zope.event import notify

from BTrees.OOBTree import OOBTree
from BTrees.OIBTree import OIBTree

from persistent import Persistent

from collective.portlet.recentactivity.interfaces import IRecentActivityUtility

class RecentActivityUtility(Persistent):
    """Recent Activity Utility
    """
    implements(IRecentActivityUtility)

    #activities = IOBTree()
    activities = None
    
    def __init__(self):
        self.activities = OOBTree()
        
    def addActivity(self, timestamp, type, user, object, parent):
        """Add an activity to the BTree.
        """

        timestamp = int(time.time())
        activity = {'type': type, 
                    'user': user, 
                    'object': object, 
                    'parent': parent}
        self.activities.insert(timestamp, activity)
        
        #from zope.container.contained import ObjectAddedEvent
        #from zope.container.contained import notifyContainerModified
        #notify(ObjectAddedEvent(object, self.activities, str(uid)))
        #notifyContainerModified(self.activities)
        return self.activities[timestamp]

    def getRecentActivity(self, items):
        """Get all activities stored in the BTree.
        """
        if self.activities:
            return self.activities.iteritems()        
            


