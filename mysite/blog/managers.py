from django.db.models import Manager
import datetime

class PublishedManager(Manager):
        """Queryset to retrieve published post"""
        
        def get_query_set(self):
            return super(PublishedManager, self).get_query_set().filter(status='p', pub_date__lte=datetime.datetime.now()) #published and in the past (future post no)
        
